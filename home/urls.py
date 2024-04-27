from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_button , name="searchButton"),
    path('insertsignup/',views.insertsignup , name="insertsignup"),
    path('logincheck/', views.logincheck , name="logincheck"),
    path('logout/', views.logout , name="logout"),
    path('seatbook/<str:searchbusid>/', views.viewseats , name="seatbook"),
    # path('proceed/<str:searchbusid>/', views.viewseats, name="proceed"),
    path('seatbookinsertsignup/<str:searchbusid>/', views.seatbookinsertsignup, name="seatbookinsertsignup"),
    path('checktask/', views.checktask , name="checktask"),
    path('bookedseat/<str:searchbusid>/', views.bookedseat, name="bookedseat"),
    path('cscdetails/', views.cancelshowchange , name="cscdetails"),
    path('cancelticket/', views.cancelticket , name="cancelticket"),
    path('updateddetails/', views.updatedetails , name="updatedetails"),
]
