
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name='index'),

    path('trip/',views.trip, name='trip'),

    path('profile/',views.profile, name='profile'),

    path('manager/',views.manager, name='manager'),

    path('manager_searched/',views.manager_search, name='manager_searched'),
    
    
    path('trip_details/<int:trip_id>',views.trip_details, name='trip_details'),

    path('trip_delete/<int:item>',views.trip_delete, name='trip_delete'),
    
    path('upcoming/',views.upcoming, name='upcoming'),

    path('reviews/',views.reviews, name='reviews'),

    path('places/',views.places, name='places'),


    path('place_searched/',views.place_searched, name='place_searched'),

    

    
    path('register/', views.sign_up, name='register'),

    path('contact/', views.contact, name='contact'),
    
    path('login/', views.Login, name='login'),

    path('logout/', views.logout_user, name='logout'),
    
    
]
