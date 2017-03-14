from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.conf import settings

# Create your views here.

class AngularApp(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(AngularApp, self).get_context_data(**kwargs)
        context['ANGULAR_URL'] = settings.ANGULAR_URL
        return context

class SampleView(View):
    def get(self, request):
        return render("HelloWorld!")
