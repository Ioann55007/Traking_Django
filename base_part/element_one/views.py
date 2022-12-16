from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.views.generic import ListView
from .forms import ContactForm
from django.views.generic.edit import FormView
from .models import BlogTemplate, Author


class OpenView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'about-us.html'


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BlogTemplateListView(ListView):
    model = BlogTemplate
    context_object_name = 'blog_in_site'



class BlogTemplateDetailView(DetailView):
    model = BlogTemplate
    template_name = 'element_one/blogtemplate-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogtemplate_list'] = BlogTemplate.objects.all()
        return context




class AuthorDetailView(DetailView):

    queryset = Author.objects.all()

    def get_object(self, **kwargs):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj



class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)




class ScheduleView(View):
    template_name = 'schedule.html'

    def get(self, request):
        return render(request, self.template_name)


class SpeakerView(View):
    template_name = 'speaker.html'

    def get(self, request):
        return render(request, self.template_name)


class GreetView(View):
    template_name = 'additional-text.html'

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})



class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

