from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path("logout",views.logout,name="logout"),
    path('book',views.book,name='book'),
    path('display',views.display,name='display'),
    path('edit/<int:id>',views.editbook,name='editbook'),
    path('update/<int:id>',views.updatebook,name='updatebook'),
     path('delete/<int:id>',views.deleterecord,name='deleterecord')
    ]