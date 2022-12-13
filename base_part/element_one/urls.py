from django.urls import path
from . import views
from .views import AuthorDetailView

app_name = 'element_one'
urlpatterns = [
    path('', views.OpenView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', views.BlogTemplateListView.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogTemplateDetailView.as_view(), name='blogtemplate-detail'),

    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    path('contact/', views.ContactView.as_view(), name='contact'),
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
    path('speaker/', views.SpeakerView.as_view(), name='speaker'),
    path('additional-text/<int:pk>/', views.GreetView.as_view(), name='additional_text'),
]
