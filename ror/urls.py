
from django.urls import path
from ror import views

urlpatterns = [
    
    path('',views.index, name="index"),
    path('index/',views.index, name="index"),
    path('login/',views.log_in, name="login"),
    path('logout/',views.log_out, name="logout"),
    path('signup/',views.sign_up, name="signup"),
    path('feedback/', views.feedback, name="feedback"),
    path('add_room/', views.add_room, name="add_room"),
    
]
