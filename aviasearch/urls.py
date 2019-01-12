from django.urls import path

from . import views



urlpatterns = [
    path('', views.aviacompany_list, name='aviacompany_list'),
    path('admin_panel', views.admin_panel, name="admin_panel"),
    path('get_aviacompany', views.get_aviacompany, name="get_aviacompany"),
    path('add_company', views.add_company, name="add_company"),
    path('add_aviacompany_page', views.add_aviacompany_page, name="add_aviacompany_page"),
    path('add_plain_page', views.add_plain_page, name="add_plain_page"),
    path('add_new_plain', views.add_new_plain, name='add_new_plain'),
    path('aviacompany_list', views.aviacompany_list, name='aviacompany_list'),
    path('delete_company_page', views.delete_company_page, name='delete_company_page'),
    path('delete_plain_page', views.delete_plain_page, name='delete_plain_page'),
    path('remove_company', views.remove_company, name='remove_company'),
    path('fleet/<int:id>/', views.fleet, name='fleet'),
    path('plain<int:id_plain>/', views.plain, name='plain'),
    path('remove_plain', views.remove_plain, name='remove_plain'),
    path('if_error', views.admin_panel, name='if_error'),
]
