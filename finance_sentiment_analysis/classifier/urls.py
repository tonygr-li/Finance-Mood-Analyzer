from django.urls import path
from . import views

urlpatterns = [
    path('', views.classifier, name='classifier'),
    #path('pdf', views.chatbotPDF, name='chatbotPDF'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('logout/', views.logout, name='logout'),
]