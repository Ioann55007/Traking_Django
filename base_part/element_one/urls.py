from django.urls import path
from . import views
app_name = 'element_one'
urlpatterns = [
    path('', views.OpenView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog-details/', views.BlogDetailView.as_view(), name='blog-details'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
    path('speaker/', views.SpeakerView.as_view(), name='speaker'),
    path('additional-text/', views.GreetView.as_view(), name='additional_text'),
]
