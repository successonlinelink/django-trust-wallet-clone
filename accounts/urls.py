from django.urls import path
from accounts import views

app_name = 'account'

urlpatterns = [
    path('', views.account, name='account'),
    path('profile/', views.my_profile, name='profile'),
    path('security/', views.security, name='security'),
    path('verify/', views.verify_account, name='verify_account'),
    path("review/", views.account_review, name="account_review"),
    
    path("change_password/", views.change_password, name="change_password"),
    path("delete_account/", views.delete_account, name="delete_account"),
    
    path("privacy/", views.privacy, name="privacy"),
    path("authority/", views.authority, name="authority"),
    path("authority/", views.authority, name="authority"),





]