import datetime
from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import formset_factory, BaseFormSet
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.views.generic import ListView
from django.views.generic.dates import WeekMixin
from django.views.generic.detail import SingleObjectMixin
from .forms import ContactForm, RegistrationForm, TestContactForm, ArticleForm
from .models import BlogTemplate, Author, Comment, Person, Blog, Alog, Logo
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.generic import FormView
from django import forms
from django.core.mail import send_mail


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


class AuthorInterestForm(forms.Form):
    name = forms.CharField()
    salutation = forms.CharField()
    email = forms.EmailField()
    headshot = forms.ImageField()
    last_accessed = forms.DateTimeField()


class AuthorDetailView(DetailView):
    model = Author

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
    object = Author.objects.all()

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)


    def get_success_url(self):
        return reverse('author-detail', kwargs={'pk': self.object.pk})



class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name']


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('element_one:author-list')


class AuthorListView(ListView):
    model = Author
    queryset = Author.objects.order_by('-last_accessed')


class RecordInterestView(SingleObjectMixin, View):
    model = Author

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden
        self.object = self.get_object()
        return HttpResponseRedirect(reverse('element_one:author-detail', kwargs={'pk': self.object.pk}))





class ScheduleView(View):
    template_name = 'schedule.html'

    def get(self, request):
        return render(request, self.template_name)


class SpeakerView(View):
    template_name = 'speaker.html'

    def get(self, request):
        return render(request, self.template_name)


class GreetView(View):
    template_name = 'additional-textarea.html'

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


class AuthorCreateView(JsonableResponseMixin, CreateView):
    model = Author
    fields = ['name', 'salutation', 'created_by', 'headshot', 'email']


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'element_one/comment_form.html'

    fields = ['author_comment', 'phone']


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'element_one/comment_detail.html'


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
    queryset = Alog.objects.order_by('-gdate')


class LogoListView(ListView):
    model = Logo
    queryset = Logo.objects.order_by('-imy_name')


class LogoDetailView(DetailView):
    model = Logo
    slug_url_kwarg = 'logo_slug'
    template_name = 'element_one/logo_detail.html'

    def get_queryset(self):
        self.object = Logo.objects.all()
        return self.object

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['logoz'] = self.object
        return context


@login_required
def profile_view(request):
    return render(request, 'element_one/profile.html')


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('element_one:profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def get_contact_test_form(request):
    if request.method == 'POST':
        form = TestContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['ioann.basic@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = TestContactForm()
    context = {'form': form}
    return render(request, 'form_snippet.html', context)


class EmailView(View):
    template_name = 'succsessfull.html'

    def post(self, request):
        return render(request, self.template_name)





def formset_view(request):
    context = {}

    # ArticleFormSet = formset_factory(ArticleForm, extra=2, max_num=1)
    # formset = ArticleFormSet(initial=[
    #          {'title': 'Django is now open source',
    #                    'pub_date': datetime.date.today(),}
    # ])
    # formset = ArticleFormSet({}, error_messages={'missing_management_form': 'Извиняюсь, пополните ПОЛЕ'})
    # formset.is_valid()
    # ArticleFormSet = formset_factory(ArticleForm, can_delete=True)
    # data = {
    #     'form-TOTAL_FORMS': '3',
    #     'form-INITIAL_FORMS': '3',
    #     'form-0-title': 'Article #1',
    #     'form-0-pub_date': '2022-12-2',
    #     'form-0-DELETE': '',
    #     'form-1-title': 'Article #2',
    #     'form-1-pub_date': '2022-12-10',
    #     'form-1-DELETE': '',
    #     'form-2-title': 'Article #3',
    #     'form-2-pub_date': '2022-12-12',
    #     'form-2-DELETE': 'on',
    # }
    # formset = ArticleFormSet(data, initial=[
    #     {'title': 'Article #1', 'pub_date': datetime.date(2022, 12, 2)},
    #     {'title': 'Article #2', 'pub_date': datetime.date(2022, 12, 10)},
    #     {'title': 'Article #3', 'pub_date': datetime.date(2022, 12, 12)}
    # ])
    class BaseArticleFormSet(BaseFormSet):
        def add_fields(self, form, index):
            super().add_fields(form, index)
            form.fields["my_field"] = forms.CharField()

    ArticleFormSet = formset_factory(ArticleForm, BaseArticleFormSet)
    formset = ArticleFormSet()
    context['formset'] = formset

    return render(request, "conact.html", context)






#













































































