
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout_user'),
    path('shop_for_services/', views.shop_for_services, name='shop_for_services'),
    path('past_order/', views.past_orders, name='past_orders'),
    path('account_manager/', views.account_manager_page, name='account_manager_page'),
    path('select_account_manager/', views.select_account_manager, name='select_account_manager'),
    path('order_complete/', views.order_complete, name='order_complete')

]
