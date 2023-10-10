
from django.urls import path 
from . import views


urlpatterns = [
    path('signuppage/', views.signuppage, name='signuppage'),
    path('signup/', views.signup, name='signup'),
    path('loginpage/', views.user_loginpage, name='loginpage'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('buy/', views.buy, name='buy'),
    #path('buyitem/<str:name>/', views.buyitem, name='buyitem'),
    path('buyitem/<str:item_name>/', views.buy_item, name='buyitem'),
    path('bought/<str:item_name>/<str:username>/<str:password>/', views.bought, name='bought'),
    path('sell/', views.sell, name='sell'),
    path('sellitem/', views.sellitem, name='sellitem'),
]

