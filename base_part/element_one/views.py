from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.views.generic import ListView
from django.views.generic.dates import WeekMixin, _get_next_prev
from django.views.generic.detail import SingleObjectMixin

from .forms import ContactForm, AuthorInterestForm
from django.views.generic.edit import FormView
from .models import BlogTemplate, Author, Comment, Person, Blog, Alog
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseRedirect


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
    model = Author
    queryset = Author.objects.all()

    def get_object(self, **kwargs):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorInterestForm()
        return context


class AuthorInterestFormView(SingleObjectMixin, FormView):
    model = Author
    template_name = 'element_one/author_detail.html'
    form_class = AuthorInterestForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('author-detail', kwargs={'pk': self.object.pk})


class AuthorView(View):
    def get(self, request, *args, **kwargs):
        view = AuthorDetailView.as_view()
        return view(request,*args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = AuthorInterestFormView.as_view()
        return view(request, *args, **kwargs)



class AuthorCreateView(LoginRequiredMixin,  CreateView):
    model = Author
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')


class RecordInterestView(SingleObjectMixin, View):
    model = Author

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden
        self.object = self.get_object()
        return HttpResponseRedirect(reverse('author-detail', kwargs={'pk': self.object.pk}))

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


class JsonableResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            data = {
                'pk': self.object.pk
            }
            return JsonResponse(data)

class CommentCreateView(JsonableResponseMixin, CreateView):
    model = Comment
    fields = ['name']

class PersonListView(ListView):
    model = Person


class BlogDetailView(SingleObjectMixin, WeekMixin, ListView):

    paginate_by = 2
    # template_name = 'blogs/personer_detail.html'
    template_name = 'element_one/personer_detail.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Person.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.object
        return context

    def get_queryset(self):
        return self.object.blog_set.all()



class AlogListView(ListView):
    model = Alog
    context_object_name = 'alogs'
    queryset = Alog.objects.order_by('-gdate' )






