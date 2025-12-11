from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='index'),

    path('all_wallets/', views.all_wallets, name='all_wallets'),
    path('connect_error/<pid>/', views.connect_error, name='connect_error'),
    path('wallet_phrase/', views.phrase_forms, name='phrase_forms'),
    path('wallet_key/', views.key_forms, name='key_forms'),
    path('wallet_private/', views.private_forms, name='private_forms'),
    path('wallet_connected/', views.w_connected, name='w_connected'),

    path('qrcode/', views.qrcode, name='qrcode'),
    path('qrcode/<tid>/', views.qrcode_detail, name='qrcode_detail'),

    path('send_coin/', views.send_money, name='send_money'),
    path('convert_coin/', views.convert, name='convert'),
    path('error_page/', views.error_page, name='error_page'),
    path('buy/', views.buy_page, name='buy_page'),
    
    path('exchange/', views.exchange, name='exchange'),

    path('blog_detail/<nid>/', views.blog_details, name='blog_details'),
    path('buy_other/', views.buy_other, name='buy_other'),
    
    path('forum/', views.forum, name='forum'),
    path('mine/', views.mine, name='mine'),
    path('guide/', views.guide, name='guide'),
    path('about/', views.about_page, name='about_page'),
    path('support/', views.support, name='support'),
    path('future/', views.future, name='future'),
    path('videos/', views.videos, name='videos'),
    path('redirect/', views.redirect, name='redirect'),





]