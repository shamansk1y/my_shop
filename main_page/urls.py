from django.urls import path
from .views import index, contacts, category_list, sub_category_list, search, update_manager, manager_list

app_name = 'main_page'



urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category_list, name='category_list'),
    path('manager/update_manager/<int:pk>', update_manager, name='update_manager'),
    path('manager/manager_list/', manager_list, name='manager_list'),
    path('category/<slug:slug>/', sub_category_list, name='sub_category_list'),
    path('search/', search, name='search'),


]