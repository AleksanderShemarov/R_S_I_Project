from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Greeting, MetroShortInfo
from django.db.models import Q
# Create your views here.


# class PreView(TemplateView):# (There is the main problem:
# TemplateView doesn't work with model and context_object_name; only with template_name
# I need to use the ListView)
#
#     model = Greeting# (!!!)
#     template_name = "greeting.html"
#     context_object_name = "greets"# (!!!)


class PreView(ListView):

    model = Greeting
    template_name = "greeting.html"
    context_object_name = 'greets'


"""def greeting_view(request):
    content = Greeting.objects.all()
    return render(request, "greeting.html", context={
        'greets' : content,
    })
# It is the work code block without Class-Based-View."""


class SearchList(ListView):

    model = MetroShortInfo
    template_name = "searching.html"
    context_object_name = "shorts"

    def get_queryset(self):
        QUERY = self.request.GET.get('rqt')
        list = MetroShortInfo.objects.filter(Q(ofiName__icontains=QUERY))
        return list


def metro_view(request):
    # Table from models.py is going here!
    infos = MetroShortInfo.objects.filter(ofiName="Prague Metro")
    return render(request, "metro.html", context={
        'INFO' : infos,
    })


class TeamTemplate(TemplateView):

    template_name = "team_page.html"


class Production(TemplateView):

    template_name = "production.html"


