from django.shortcuts import render,redirect,HttpResponse
# from .models import location,customer,bus
from .models import *
from django.db import connection
# from django.http import JsonResponse
from datetime import datetime, timedelta
import calendar
import base64
import json
# import razorpay
from django.conf import settings
import smtplib,ssl
from email.message import EmailMessage
import pandas as pd


with connection.cursor() as cursor:
    cursor.execute("SELECT routedict FROM home_checkroute WHERE checkrid=%s",['C1'])
    routedict = cursor.fetchone()
    
    
routecheckdict = eval(routedict[0])
# print(routecheckdict,type(routecheckdict))

locations = location.objects.all()
context = {
    'locations' : locations,
    'account_name' : None,
    'account_id' : None,
}

action = {
    'action' : None,
}


# Create your views here.
def home(request):
    return render(request, 'home/home.html',context)

def search_button(request):
    global flag 
    global searchinfo
    source = request.POST.get('from',False)
    destination = request.POST.get('to',False)
    date = datetime.strptime(request.POST.get('traveldate',False),'%Y-%m-%d')
    day = date.strftime('%a')
    year = date.year
    d = date.strftime('%d')
    month = calendar.month_abbr[date.month]
    # print(source,destination,day,d,month,year)

    # print(day,type(day))
    goingRoute = source + '-' + destination
    returnRoute = destination + '-' + source
    # print(goingRoute,returnRoute)
    daylist = ['Tue','Thu','Sat']
    if day in daylist:
        if routecheckdict[goingRoute] != 1 and routecheckdict[returnRoute] != 1: 

            query4 = "SELECT rid FROM home_route WHERE routeway IN (%s , %s)"
            with connection.cursor() as cursor:
                cursor.execute(query4,[goingRoute,returnRoute])
                rids1 = cursor.fetchall()
                # print(rids1,"\n",rids1[0][0],rids1[1][0])
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE home_bus SET rid_id = %s WHERE rid_id = %s",["TEMP",rids1[0][0]])
                cursor.execute("UPDATE home_bus SET rid_id = %s WHERE rid_id = %s",[rids1[0][0],rids1[1][0]])
                cursor.execute("UPDATE home_bus SET rid_id = %s WHERE rid_id = %s",[rids1[1][0],"TEMP"])
            
            routecheckdict[goingRoute] = 1
            routecheckdict[returnRoute] = 1
            with connection.cursor() as cursor:
                cursor.execute("UPDATE home_checkroute SET routedict = %s WHERE checkrid = %s",[str(routecheckdict),'C1'])
    else:
        if routecheckdict[goingRoute] == 1 and routecheckdict[returnRoute] == 1:
            query5 = "SELECT rid FROM home_route WHERE routeway IN (%s , %s)"
            with connection.cursor() as cursor:
                cursor.execute(query5,[goingRoute,returnRoute])
                rids2 = cursor.fetchall()
                # print(rids2,"\n",rids2[0][0],rids2[1][0])
            
            with connection.cursor() as cursor:
                            #"UPDATE home_bus SET rid_id = %s WHERE rid_id = %s"
                cursor.execute("UPDATE home_bus SET rid_id = %s WHERE rid_id = %s",["TEMP",rids2[0][0]])
                cursor.execute("UPDATE home_bus SET rid_id = %s WHERE rid_id = %s",[rids2[0][0],rids2[1][0]])
                cursor.execute("UPDATE home_bus SET rid_id = %s WHERE rid_id = %s",[rids2[1][0],"TEMP"])


            routecheckdict[goingRoute] = 0
            routecheckdict[returnRoute] = 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE home_checkroute SET routedict = %s WHERE checkrid = %s",[str(routecheckdict),'C1'])
               
        
    
    # print(routecheckdict)


    if context['account_name'] == None:
        searchinfo = {
            'source' : source,
            'destination' : destination,
            'date' : d,
            'month' : month,
            'year' : year,
            'day' : day ,
        }
    else:
        searchinfo = {
            'source' : source,
            'destination' : destination,
            'date' : d,
            'month' : month,
            'year' : year,
            'day' : day ,
            'account_name': context['account_name'],
        }

    rout = source + "-" + destination
    # print(rout)
    query1 = "SELECT rid FROM home_route WHERE routeway = %s"
    with connection.cursor() as cursor:
        cursor.execute(query1,[rout])
        rid = cursor.fetchone()
        # print(rid)       
    
    query2 = "SELECT * FROM home_bus WHERE rid_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query2,[rid])
        busdata = cursor.fetchall()
        # print(busdata)
        # searchinfo['busdata'] = busdata    

    busid = []
    for i in busdata:
        busid.append(i[0])
    busid = tuple(busid)
    # print(busid,type(busid))

    
    images = []
    for id in busid:
        query3 = "SELECT image FROM home_busImage WHERE bid_id = %s"  
        with connection.cursor() as cursor:
            cursor.execute(query3, id)
            result = cursor.fetchall()
            # print(len(images))
        images.append(result)
    
    images = tuple(images)
    # print(images)
    mainimages = []
    test = []
    for i in images:
        for j in range(len(i)):
            test.append(base64.b64encode(i[j][0]).decode('utf-8'))
        mainimages.append(tuple(test))
        test.clear()
    
    mainimages = tuple(mainimages)
    
    busdetials = []
    for index,data in enumerate(busdata):
        
        testlist = list(data)
        testlist.append(mainimages[index])

        busdetials.append(tuple(testlist))
       
    # searchinfo['images'] = result_tuples
    busdetials = tuple(busdetials)
    # print(busdetials)

    searchinfo['busdata'] = busdetials
    # print(searchinfo.keys())

    


    return render(request, 'home/searchpanel.html',searchinfo)

def insertsignup(request):
    if context['account_name'] == "invalid":
        context['account_name'] = None
    fname = request.POST['fname']
    lname = request.POST['lname']
    gend = request.POST['gender']
    a = request.POST['age']
    ph = request.POST['phone']
    eid = request.POST['email']
    user = request.POST['uname']
    passw = request.POST['cpwd']

    query = "SELECT name FROM home_customer WHERE email = %s"
    with connection.cursor() as cursor:
        cursor.execute(query,[eid])
        name = cursor.fetchone()
    # print(name)
    if name: 
        context['account_name'] = "incorrect"
        return render(request, 'home/home.html',context)
    else:
        n = fname + ' ' + lname
        n = n.title()
        prefix = 'C00'
        total_cust = customer.objects.all().count()
        cid = prefix + str(total_cust + 1)
        # print(n,gend,a,ph,eid,user,passw,cid) 

        cu = customer(custid=cid, name=n, gender=gend, age=a, phone=ph, email=eid, username=user, password=passw)
        cu.save()
        context['account_name'] = n
        context['account_id'] = cid
        return render(request, 'home/home.html',context)

def logincheck(request):
    user = request.POST['lusername']
    passw = request.POST['lpassword']

    # print(user,passw)

    query = "SELECT name,custid FROM home_customer WHERE username = %s AND password = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, [user, passw])
        name = cursor.fetchone()  

        if name:
            context['account_name'] = name[0]
            context['account_id'] = name[1]
        else:
            context['account_name'] = "invalid"

    return render(request, 'home/home.html',context)
    
def logout(request):
    context['account_name'] = None
    context['account_id'] = None
    return render(request, 'home/home.html',context)

def viewseats(request,searchbusid):
    global searchdetails
    searchdetails = {'source':searchinfo['source'],'destination':searchinfo['destination'],'date':searchinfo['date'],'month':searchinfo['month'],'year':searchinfo['year'],'day':searchinfo['day']}
    print(searchbusid)
    query1 = "SELECT * FROM home_bus WHERE bid = %s"
    with connection.cursor() as cursor:
        cursor.execute(query1,[searchbusid])
        searchbusdata = cursor.fetchone()
    
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT BDpoints,address FROM home_boardingdropping WHERE city=%s",[searchinfo['source']])
        sourcepoints = cursor.fetchall()
    with connection.cursor() as cursor:
        cursor.execute("SELECT BDpoints,address FROM home_boardingdropping WHERE city=%s",[searchinfo['destination']])
        destinationpoints = cursor.fetchall()
    boarddroppoints = sourcepoints + destinationpoints
    print(boarddroppoints) 
    

    searchdetails['searchbusdata'] = searchbusdata
    if searchdetails['searchbusdata'][2] == 'AC / Sleeper':
        searchdetails['typecheck'] = 'yes'
    else:
        searchdetails['typecheck'] = 'no'
    
    boardingtimelist = []
    boardingtimestring = searchbusdata[3]
    boardingtimelist.append(boardingtimestring)
    for i in range(0,len(json.loads(boarddroppoints[0][0]))-1):
        boardingtime = datetime.strptime(boardingtimestring, '%I:%M %p')
        newtime = boardingtime + timedelta(minutes=15)
        newtimestring = newtime.strftime('%I:%M %p')
        boardingtimelist.append(newtimestring)
        boardingtimestring = newtimestring
    print(boardingtimelist)

    droppingtimelist = []
    droppingtimestring = searchbusdata[4]
    droppingtimelist.append(droppingtimestring)
    for i in range(0,len(json.loads(boarddroppoints[1][0]))-1):
        droppingtime = datetime.strptime(droppingtimestring, '%I:%M %p')
        newtime = droppingtime - timedelta(minutes=15)
        newtimestring = newtime.strftime('%I:%M %p')
        droppingtimelist.append(newtimestring)
        droppingtimestring = newtimestring
    droppingtimelist = list(reversed(droppingtimelist))
    print(droppingtimelist)


    boardingpoints = zip(boardingtimelist,json.loads(boarddroppoints[0][0]),json.loads(boarddroppoints[0][1]))
    # print(boardingpoints)
    droppingpoints = zip(droppingtimelist,json.loads(boarddroppoints[1][0]),json.loads(boarddroppoints[1][1]))
    
    searchdetails['boardingpoints'] = boardingpoints
    searchdetails['droppingpoints'] = droppingpoints
    searchdetails['account_name'] = context['account_name']       
    searchdetails['account_id'] = context['account_id']

    if context['account_id'] != None :
        query3 = "SELECT email,phone FROM home_customer WHERE custid = %s"
        with connection.cursor() as cursor:
            cursor.execute(query3,[context['account_id']])
            email_phone = cursor.fetchone()
            print(email_phone)
            searchdetails['cust_email'] = email_phone[0]
            searchdetails['cust_phone'] = email_phone[1] 

    traveldate = searchinfo['date']+ " " + searchinfo['month'] + " " + str(searchinfo['year'])
    traveldate = datetime.strptime(traveldate, "%d %b %Y")
    query4 = "SELECT reservid FROM home_reservation WHERE bid_id = %s AND reservDate= %s"
    with connection.cursor() as cursor:
        cursor.execute(query4,[searchbusid,traveldate])
        freservationsid = cursor.fetchall()
        # print(len(freservationsid))
    seatnumbers = []
    if len(freservationsid) != 0:
        reservationsid = []
        for i in range(len(freservationsid)):
            reservationsid.append(freservationsid[i][0])
        # print(reservationsid)

        query5 = "SELECT seatnumbers FROM home_seatassignment WHERE reservid_id IN %s"
        with connection.cursor() as cursor:
            cursor.execute(query5,[reservationsid])
            fseatnumbers = cursor.fetchall()
            # print(fseatnumbers)
        
        for i in range(len(fseatnumbers)):
            emp_list = eval(fseatnumbers[i][0])
            for j in emp_list:
                seatnumbers.append(j)
        # print(seatnumbers)
    searchdetails['bookedseatno'] = seatnumbers

    # client = razorpay.Client(auth = (settings.KEY , settings.SECRET))
    # payment = client.order.create({'amount' : 1000 * 100,'currency' : 'INR' , 'payment_capture' : 1})


    # print("*************")
    # print(payment)
    # print("*************")
    # searchdetails['payment'] = payment
    print(searchdetails)
    return render(request,'home/seatbook.html',searchdetails)


def seatbookinsertsignup(request,searchbusid):
    if context['account_name'] == "invalid":
        context['account_name'] = None
        searchdetails['account_name'] = context['account_name']
    fname = request.POST['fname']
    lname = request.POST['lname']
    gend = request.POST['gender']
    a = request.POST['age']
    ph = request.POST['phone']
    eid = request.POST['email']
    user = request.POST['uname']
    passw = request.POST['cpwd']

    query = "SELECT name FROM home_customer WHERE email = %s"
    with connection.cursor() as cursor:
        cursor.execute(query,[eid])
        name = cursor.fetchone()
    # print(name)
    if name: 
        context['account_name'] = "incorrect"
        searchdetails['account_name'] = context['account_name']
        # return render(request, 'home/home.html',context)
        # return render(request,'home/seatbook.html',searchdetails)
        return redirect("seatbook",searchbusid=searchbusid)

    else:
        n = fname + ' ' + lname
        n = n.title()
        prefix = 'C00'
        total_cust = customer.objects.all().count()
        cid = prefix + str(total_cust + 1)
        # print(n,gend,a,ph,eid,user,passw,cid) 

        cu = customer(custid=cid, name=n, gender=gend, age=a, phone=ph, email=eid, username=user, password=passw)
        cu.save()
        context['account_name'] = n
        context['account_id'] = cid
        searchdetails['account_name'] = context['account_name']
       
        return redirect("seatbook",searchbusid=searchbusid)


def checktask(request):
    # global action
    ticket_action = request.GET.get('ticket_action')
    # print(ticket_action,type(ticket_action))
    action['action'] = ticket_action
    action['account_name'] = context['account_name']
    action['cancellationdatecheck'] = None
    action['changedetailsdatecheck'] = None
    action['reservationcheck'] = None
    action['updatestatus'] = None
    return render(request,'home/checktask.html',action)


def sendmail(ticketdetails,emailpassengerdata):
    sender_email = "HappyRide1415@outlook.com"
    password = "HappyJourney"
    allSeatNumber,passengersName,passengersAge,passengersGender = zip(*emailpassengerdata)
    df = pd.DataFrame({'Seat No':allSeatNumber,'Name':passengersName,'Age':passengersAge,'Gender':passengersGender})
    html_table = df.to_html(index=False)  

    try:
        message = EmailMessage()
        message["From"] = sender_email
        message["To"] = searchdetails['cust_email']
        message["Subject"] = "Reservation Ticket"


        message.add_alternative("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bus Reservation System</title>
        <style>
        * {{
        margin: 0;
        padding: 0;
        }}

        body {{
        /* background-color: #898ae6; */
        background-color: #d7d6fe;
        }}

        .outerdiv {{
        display: flex;
        justify-content: center;
        margin: 2% 0%;
        font-size: larger;
        }}

        .innerdiv {{
        text-align: center;
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        }}

        .reservationtext, .boarding, .dropping , .busnumber, .paymentstatus {{
        text-align: left;
        margin-bottom: 5px;
        }}

        .traveldate {{
        text-align: right;
        }}

        .note {{
        font-size: large;
        color: #FF474C;
        }}

                                
        table {{
        border-collapse: collapse; 
        }}
                                
        th, td {{
        padding: 15px;
        border: 1px solid black; 
        }}
        </style>
        </head>

        <body>
        <div class="outerdiv">
        <div class="innerdiv">
        <h2>HappyRide</h2>
        <div class="traveldate">
        Travel Date : {0}
        </div>
        <div class="reservationtext">
        Your Reservation ID : {1}
        </div>
        <div class="busnumber">
        Bus Number: {2}
        </div>
        <div class="boarding">
        Boarding : {3} <br>
        Boarding Address : {4}
        </div>
        <div class="dropping">
        Dropping : {5} <br>
        Dropping Address : {6}
        </div>
        <div class="paymentstatus">
        Payment Status : {8}
        </div>
        <h3>
        Passenger Details : {7}
        </h3>
        <div class="note">
        Please note your Reservation ID
        </div>
        </div>
        </div>
        </body>

        </html>
                """.format(ticketdetails['traveldate'],ticketdetails['reservationid'],ticketdetails['busnumber'],ticketdetails['boarding'],ticketdetails['boardingadd'],ticketdetails['dropping'],ticketdetails['droppingadd'],html_table,ticketdetails['paymentstatus']),subtype='html')

        print(ticketdetails['passengersdata'],type(ticketdetails['passengersdata']))
        context = ssl.create_default_context()
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls(context=context)
            smtp.ehlo()
            smtp.login(sender_email, password)
            smtp.send_message(message)
            print('Mail Sent')
    except:
        print("error")


def bookedseat(request,searchbusid):
    boardingPtAdd = request.POST['boarding']
    droppingPtAdd = request.POST['dropping']
    passengersName = request.POST.getlist('Pname')
    passengersGender = request.POST.getlist('Pgender')
    passengersAge = request.POST.getlist('Page')
    totalamount = int(request.POST['TravelTotalAmount'])
    allSeatNumber = request.POST.getlist('AllPassengerSeatNO')
    paymentstatus = request.POST['checkpaymentstatus']
    tdate = request.POST['Tdate']
    showdate = tdate
    tdate = datetime.strptime(tdate, "%d %b %Y")
    boardingPtAdd = boardingPtAdd.split(" / ")
    droppingPtAdd = droppingPtAdd.split(" / ")
    print()
    # print(boardingPtAdd,droppingPtAdd)
    # print(passengersName,passengersGender,passengersAge)
    # print(searchbusid,searchdetails['account_id'])
    # print(tdate,type(tdate),totalamount,type(totalamount),allSeatNumber)
    searchbusid_fk = bus.objects.get(bid=searchbusid)
    customerid_fk = customer.objects.get(custid=searchdetails['account_id'])
    routeid_fk = route.objects.get(rid=searchdetails['searchbusdata'][7])
    reservprefix = 'RSV00'
    total_reserv = reservation.objects.all().count()
    plusone_reserv = total_reserv + 1
    rid = reservprefix + str(total_reserv + 1)
    with connection.cursor() as cursor:
        cursor.execute("SELECT reservid FROM home_reservation")
        allreserid = cursor.fetchall()
        # print(allreserid)
    allreseridlist = []
    for i in allreserid:
        allreseridlist.append(i[0])
    # print(allreseridlist)
    if rid in allreseridlist:
        rid = reservprefix + str(plusone_reserv + 1)
    # print(rid)
        
    reserv = reservation(reservid=rid, bid=searchbusid_fk, custid=customerid_fk, rid=routeid_fk , reservDate=tdate, totalAmount=totalamount, boardingPoint=boardingPtAdd[0], boardingAddress=boardingPtAdd[1], droppingPoint=droppingPtAdd[0], droppingAddress=droppingPtAdd[1], paymentStatus=paymentstatus)
    reserv.save()

    rid_fk = reservation.objects.get(reservid=rid)
    for i in range(len(passengersName)):
        passenprefix = 'P00'
        total_passen = passengerdetails.objects.all().count()
        plusonepassenid = total_passen + 1
        pid = passenprefix + str(total_passen + 1)
        with connection.cursor() as cursor:
            cursor.execute("SELECT passengerid FROM home_passengerdetails")
            allpassenid = cursor.fetchall()
        # print(allpassenid)
        allpassenidlist = []
        for j in allpassenid:
            allpassenidlist.append(j[0])
        # print(allpassenidlist)
        if pid in allpassenidlist:
            pid =  passenprefix + str(plusonepassenid + 1)
        # print(pid)
        passen = passengerdetails(passengerid=pid, reservid=rid_fk, name=passengersName[i], gender=passengersGender[i], age=passengersAge[i])
        passen.save()
        
    seatsassign = seatassignment(reservid=rid_fk, seatnumbers=str(allSeatNumber))
    seatsassign.save()
    # print(rid,customerid_fk,searchbusid_fk)
    passengersdata = zip(allSeatNumber,passengersName,passengersAge,passengersGender)
    ticketdetails = {"traveldate":showdate,"reservationid":rid,"busnumber":searchdetails['searchbusdata'][1],"boarding":boardingPtAdd[0],"boardingadd":boardingPtAdd[1],"dropping":droppingPtAdd[0],"droppingadd":droppingPtAdd[1],"passengersdata":passengersdata,"paymentstatus":paymentstatus}

    emailpassengerdata = zip(allSeatNumber,passengersName,passengersAge,passengersGender)
    sendmail(ticketdetails,emailpassengerdata)

    return render(request,'home/bookedseat.html',ticketdetails)

def cancelshowchange(request):
    global reserv_details
    reserv_id = request.POST['reservation-id']
    email = request.POST['email']
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM home_reservation WHERE reservid = %s",[reserv_id])
        reserv_details = cursor.fetchone()
    
    print(reserv_details)
    if reserv_details == None:
        # return redirect('checktask')
        action['reservationcheck'] = "incorrect"
        action['cancellationdatecheck'] = None
        action['changedetailsdatecheck'] = None
        action['updatestatus'] = None
        return render(request,'home/checktask.html',action)

    with connection.cursor() as cursor:
        cursor.execute("SELECT email FROM home_customer WHERE custid = %s",[reserv_details[9]])
        checkemail = cursor.fetchone()
    
    if checkemail[0] != email:
        print("incorrect email")
   
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM home_passengerdetails WHERE reservid_id = %s",[reserv_id])
        passendata = cursor.fetchall()
    # print(passendata)
    date_obj = datetime.strptime(str(reserv_details[1]), '%Y-%m-%d')
    reserv_date = date_obj.strftime('%d %b %Y')
    print(reserv_date,date_obj)

    with connection.cursor() as cursor:
        cursor.execute("SELECT seatnumbers FROM home_seatassignment WHERE reservid_id = %s",[reserv_id])
        seatnumbers = cursor.fetchone()
        print(seatnumbers)
    seatnumbers = eval(seatnumbers[0])
    
    global passengers_id
    passengers_id = []
    passengers_name = []
    passengers_age = []
    passengers_gender = []
    for i in range(len(passendata)):
        for j in range(len(passendata[i])):
            if j == 0: 
                passengers_id.append(passendata[i][j])
            if j == 1:
                passengers_name.append(passendata[i][j])
            if j == 2:
                passengers_gender.append(passendata[i][j])
            if j == 3:
                passengers_age.append(passendata[i][j])

    print(passengers_id,passengers_name,passengers_gender,passengers_age,seatnumbers)

    if action['action'] == "Show My Ticket":
        boardingtimepoint = reserv_details[3].split(' ',2)
        droppingtimepoint = reserv_details[5].split(' ',2)
        
        showmyticketdetails = {
            'reserv_date' : reserv_date,
            'boardingpoint' : boardingtimepoint[2],
            'droppingpoint' : droppingtimepoint[2],
            'boardingtime' : boardingtimepoint[0] + ' ' + boardingtimepoint[1],
            'droppingtime' : droppingtimepoint[0] + ' ' + droppingtimepoint[1],
            'boardingadd' : reserv_details[4],
            'droppingadd' : reserv_details[6],
            'passengersdeatils' : zip(passengers_name,seatnumbers,passengers_gender,passengers_age)
        }
        return render(request,'home/showmyticket.html',showmyticketdetails)

    elif action['action'] == "Cancel Ticket":
        current_date = datetime.now()
        if date_obj < current_date:
            action['reservationcheck'] = None
            action['changedetailsdatecheck'] = None
            action['updatestatus'] = None
            action['cancellationdatecheck'] = 'incoorectdate'
            return render(request,'home/checktask.html',action)

        with connection.cursor() as cursor:
            cursor.execute("SELECT amount FROM home_bus WHERE bid = %s",[reserv_details[8]])
            perpersonamount = cursor.fetchone()

        with connection.cursor() as cursor:
            cursor.execute("SELECT routeway FROM home_route WHERE rid = %s",reserv_details[10])
            sourcedestination = cursor.fetchone()
            sourcedestination = sourcedestination[0].split('-')
            # print(sourcedestination)
            cancel_details = {
                'source' : sourcedestination[0],
                'destination' : sourcedestination[1],
                'reservid' : reserv_details[0],
                'reserv_date' : reserv_date,
                'perpersonamount' : perpersonamount[0],
                'totalamount' : reserv_details[2],
                'passengersdeatils' : zip(passengers_id,passengers_name,passengers_age,passengers_gender,seatnumbers)
            }
        print(cancel_details)
        return render(request,'home/cancelpage.html',cancel_details)
    elif action['action'] == "Change Details":
        current_date = datetime.now()
        if date_obj < current_date:
            action['reservationcheck'] = None
            action['cancellationdatecheck'] = None
            action['updatestatus'] = None
            action['changedetailsdatecheck'] = 'incoorectdate'
            return render(request,'home/checktask.html',action)
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT routeway FROM home_route WHERE rid=%s",[reserv_details[10]])
            routeway = cursor.fetchone()
            routeway = routeway[0].split('-')
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT departureTime,arrivalTime FROM home_bus WHERE bid=%s",[reserv_details[8]])
            bdtime = cursor.fetchone()

        
        # query2 = "SELECT BDpoints,address FROM home_boardingdropping WHERE city=%s OR city=%s"
        with connection.cursor() as cursor:
            cursor.execute("SELECT BDpoints,address FROM home_boardingdropping WHERE city=%s",[routeway[0]])
            sourcepoints = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute("SELECT BDpoints,address FROM home_boardingdropping WHERE city=%s",[routeway[1]])
            destinationpoints = cursor.fetchall()
            # print(boarddroppoints) 
        boarddroppoints = sourcepoints + destinationpoints
        boardingtimelist = []
        boardingtimestring = bdtime[0]
        boardingtimelist.append(boardingtimestring)
        for i in range(0,len(json.loads(boarddroppoints[0][0]))-1):
            boardingtime = datetime.strptime(boardingtimestring, '%I:%M %p')
            newtime = boardingtime + timedelta(minutes=15)
            newtimestring = newtime.strftime('%I:%M %p')
            boardingtimelist.append(newtimestring)
            boardingtimestring = newtimestring
        # print(boardingtimelist)

        droppingtimelist = []
        droppingtimestring = bdtime[1]
        droppingtimelist.append(droppingtimestring)
        for i in range(0,len(json.loads(boarddroppoints[1][0]))-1):
            droppingtime = datetime.strptime(droppingtimestring, '%I:%M %p')
            newtime = droppingtime - timedelta(minutes=15)
            newtimestring = newtime.strftime('%I:%M %p')
            droppingtimelist.append(newtimestring)
            droppingtimestring = newtimestring
        droppingtimelist = list(reversed(droppingtimelist))
        # print(droppingtimelist)


        boardingpoints = zip(boardingtimelist,json.loads(boarddroppoints[0][0]),json.loads(boarddroppoints[0][1]))
        # print(boardingpoints)
        droppingpoints = zip(droppingtimelist,json.loads(boarddroppoints[1][0]),json.loads(boarddroppoints[1][1]))
        
        
        changedetails = {
            'passengersdetails' : zip(passengers_id,passengers_name,passengers_age,passengers_gender,seatnumbers),
            'boardingpoints' : boardingpoints,
            'droppingpoints' : droppingpoints,
        }
        return render(request,'home/updatepassengersdetails.html',changedetails)

    # return HttpResponse(action['action'])

def cancelticket(request):
    cpassenger = request.POST.getlist('cancelpassenger')
    updatedamount = request.POST['updatedamount']
    urefundamount = request.POST['urefundamount']
    passengerlist = []
    seatsnumberlist = []
    for i in cpassenger:
        a = i.split(' ')
        for j in range(len(a)):
            if j == 0:
                passengerlist.append(a[j])
            else:
                seatsnumberlist.append(a[j])
        # print(a)
    # print(cpassenger)
    # print(urefundamount,updatedamount)
    # print(passengerlist,seatsnumberlist)
    cancelpassengers = []
    for passid in passengerlist:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_passengerdetails WHERE passengerid = %s",[passid])
            cancelpassengers.append(list(cursor.fetchone()))
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT seatnumbers FROM home_seatassignment WHERE reservid_id = %s",[reserv_details[0]])
        allseatsnumberlist = cursor.fetchone()
        allseatsnumberlist = eval(allseatsnumberlist[0])
        

    # print(cancelpassengers)
    # print(allseatsnumberlist,type(allseatsnumberlist))

    cpassengername = []
    cpassengergender = []
    cpassengerage = []
    for i in range(len(cancelpassengers)):
        for j in range(len(cancelpassengers[i])):
            if j == 1:
                cpassengername.append(cancelpassengers[i][j])
            if j == 2:
                cpassengergender.append(cancelpassengers[i][j])
            if j == 3:
                cpassengerage.append(cancelpassengers[i][j])
    print(cpassengername,cpassengergender,cpassengerage)
    cancelpassengersdetails = {
        'cancelpassengers' : zip(seatsnumberlist,cpassengername,cpassengerage,cpassengergender),
        'refundableamount' : urefundamount,
    }

    if len(seatsnumberlist) == len(allseatsnumberlist):
        print("all data should be deleted")
        for i in passengerlist:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM home_passengerdetails WHERE passengerid = %s",[i])
                connection.commit()
        
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM home_seatassignment WHERE reservid_id = %s",[reserv_details[0]])
        
        cancelpassenprefix = 'CAN00'
        total_cancelpassen = cancellation.objects.all().count()
        caid = cancelpassenprefix + str(total_cancelpassen + 1)
        custid_fk = customer.objects.get(custid=reserv_details[9])
        rservid_fk = reservation.objects.get(reservid=reserv_details[0])
        canceltable = cancellation(cancelid=caid, custid=custid_fk, resverid=rservid_fk, cancelAmount=urefundamount)
        canceltable.save()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM home_reservation WHERE reservid = %s",[reserv_details[0]])

    else:
        print("only selected data should be deleted")
        for dseat in seatsnumberlist:
            allseatsnumberlist.remove(dseat)
            
        for i in passengerlist:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM home_passengerdetails WHERE passengerid = %s",[i])
                connection.commit()
        
        with connection.cursor() as cursor:
            cursor.execute("UPDATE home_seatassignment SET seatnumbers = %s WHERE reservid_id = %s",[str(allseatsnumberlist),reserv_details[0]])
        
        with connection.cursor() as cursor:
            cursor.execute("UPDATE home_reservation SET totalAmount = %s WHERE reservid = %s",[updatedamount,reserv_details[0]])
        cancelpassenprefix = 'CAN00'
        total_cancelpassen = cancellation.objects.all().count()
        caid = cancelpassenprefix + str(total_cancelpassen + 1)
        custid_fk = customer.objects.get(custid=reserv_details[9])
        rservid_fk = reservation.objects.get(reservid=reserv_details[0])
        canceltable = cancellation(cancelid=caid, custid=custid_fk, resverid=rservid_fk, cancelAmount=urefundamount)
        canceltable.save()
    
    return render(request,'home/showcanceldetails.html',cancelpassengersdetails)

def updatedetails(request):
    passengersid = request.POST.getlist('passengerId')
    upassengersname = request.POST.getlist('passengerName')
    upassengersgender = request.POST.getlist('gender')
    upassengersage = request.POST.getlist('passengerAge')
    try:
        uboarding = request.POST['boarding']
        udropping = request.POST['dropping']
    except:
        uboarding = reserv_details[3] + ' / ' + reserv_details[4]
        udropping = reserv_details[5] + ' / ' + reserv_details[6]
    uboarding = uboarding.split(' / ')
    udropping = udropping.split(' / ')

    for i in range(len(passengersid)):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE home_passengerdetails SET name = %s, gender = %s, age = %s WHERE passengerid = %s",[upassengersname[i],upassengersgender[i],upassengersage[i],passengersid[i]])

    with connection.cursor() as cursor:
        cursor.execute("UPDATE home_reservation SET boardingPoint = %s, boardingAddress = %s, droppingPoint = %s, droppingAddress = %s WHERE reservid = %s",[uboarding[0],uboarding[1],udropping[0],udropping[1],reserv_details[0]])

    action['cancellationdatecheck'] = None
    action['reservationcheck'] = None
    action['changedetailsdatecheck'] = None
    action['updatestatus'] = 'successful'

    # print(passengersid,upassengersname,upassengersgender,upassengersage,uboarding,udropping)
    return render(request,'home/checktask.html',action)
    
