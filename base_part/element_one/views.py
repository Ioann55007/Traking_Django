from django.shortcuts import render
from django.views import View


class OpenView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(View):
    template_name = 'about-us.html'

    def get(self, request):
        return render(request, self.template_name)


class BlogView(View):
    template_name = 'blog.html'

    def get(self, request):
        return render(request, self.template_name)


class BlogDetailView(View):
    template_name = 'blog-details.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)


class MainView(View):
    template_name = 'main.html'

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

    def get(self, request):
        return render(request, self.template_name)


