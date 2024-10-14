from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def my_func(request):
    return render(request, 'func_template.html')


class SomeClass(TemplateView):
    template_name = 'class_template.html'
