from django.contrib.auth.models import User
from django.urls import path
from . import views
from .models import Alog
from .views import AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, RecordInterestView, \
    BlogDetailView, PersonListView, AlogListView, LogoListView, LogoDetailView, profile_view, RegisterView, \
    CommentCreateView, CommentDetailView, AuthorListView, AuthorInterestFormView, get_contact_test_form, \
     formset_view
from django.views.generic.dates import ArchiveIndexView
app_name = 'element_one'





urlpatterns = [
    path('', views.OpenView.as_view(), name='index'),
    path('profile/', profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', views.BlogTemplateListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.BlogTemplateDetailView.as_view(), name='blogtemplate-detail'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author-list/', AuthorListView.as_view(), name='author-list'),
    path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    path('author/<int:pk>/interest/', RecordInterestView.as_view(), name='author-interest'),
    path('authors/<int:pk>/interest/', AuthorInterestFormView.as_view(), name='author-interests'),
    path('person-list/', PersonListView.as_view(), name='person-blog'),
    path('person-detail/<int:pk>/', BlogDetailView.as_view(), name='person_detail'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
    path('speaker/', views.SpeakerView.as_view(), name='speaker'),
    path('additional-text/<int:pk>/', views.GreetView.as_view(), name='additional_text'),
    path('alog-list/', AlogListView.as_view(), name = 'alog-list'),
    path('archive/', ArchiveIndexView.as_view(model = Alog, date_field='gdate'), name = 'alog_archive'),
    path('logo/', LogoListView.as_view(), name = 'logo_list'),
    path('logo_detail/<slug:logo_slug>/', LogoDetailView.as_view(), name = 'logo_detail'),
    path('comment/add/', CommentCreateView.as_view(), name='comment'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name = 'comment_detail'),
    path('email-get/', get_contact_test_form, name='get_email'),
    path('thanks/', views.EmailView.as_view(), name='thanks'),
    path('conact/', formset_view, name='conact'),

]
