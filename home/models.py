from django.db import models

# Create your models here.

class location(models.Model):
    lid = models.CharField(max_length=100,primary_key=True)
    loc = models.CharField(max_length=100)

class checkroute(models.Model):
    checkrid = models.CharField(max_length=100,primary_key=True)
    routedict = models.CharField(max_length=500)

class customer(models.Model):
    custid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=250)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)  
 
class route(models.Model):
    rid = models.CharField(max_length=10, primary_key=True)
    routeway = models.CharField(max_length=150)

class bus(models.Model):
    bid = models.CharField(max_length=100,primary_key=True)
    rid = models.ForeignKey(route, on_delete=models.CASCADE)
    busNumber = models.CharField(max_length=255)
    busType = models.CharField(max_length=255)
    departureTime = models.CharField(max_length=50)
    arrivalTime = models.CharField(max_length=50)
    totalTime = models.CharField(max_length=50)
    amount = models.IntegerField()

class busImage(models.Model):
    bid = models.ForeignKey(bus, on_delete=models.CASCADE)
    image = models.BinaryField()

class BoardingDropping(models.Model):
    city = models.CharField(max_length=100,primary_key=True)
    BDpoints = models.TextField()
    address = models.TextField()

class reservation(models.Model):
    reservid = models.CharField(max_length=100,primary_key=True)
    bid = models.ForeignKey(bus, on_delete=models.CASCADE)
    custid = models.ForeignKey(customer, on_delete=models.CASCADE)
    rid = models.ForeignKey(route, on_delete=models.CASCADE)
    reservDate = models.DateField()    
    totalAmount = models.IntegerField()  
    boardingPoint = models.CharField(max_length=100)
    boardingAddress = models.TextField()
    droppingPoint = models.CharField(max_length=100)
    droppingAddress = models.TextField()  
    paymentStatus = models.CharField(max_length=100)

# datefield store date in 'YYYY-MM-DD' 
    
class passengerdetails(models.Model):
    passengerid = models.CharField(max_length=100,primary_key=True)
    reservid = models.ForeignKey(reservation, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    

class seatassignment(models.Model):
    reservid = models.ForeignKey(reservation, on_delete=models.CASCADE)
    seatnumbers = models.TextField()

class cancellation(models.Model):
    cancelid = models.CharField(max_length=100,primary_key=True)
    custid = models.ForeignKey(customer, on_delete=models.CASCADE)
    resverid = models.ForeignKey(reservation, on_delete=models.CASCADE)
    cancelAmount = models.IntegerField()
