from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, TemplateView, FormView
from .models import Greeting, MetroShortInfo, UserFormReg, UserEnter
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
    if request.method == "GET":
        # Table from models.py is going here!
        infos = MetroShortInfo.objects.filter(ofiName="Prague Metro")
        return render(request, "metro.html", context={
            'INFO' : infos,
        })
    elif request.method == "POST":
        infos = MetroShortInfo.objects.filter(ofiName="Prague Metro")
        return render(request, "metro.html", context={
            'INFO': infos,
        })
    return HttpResponse("""
        <div>
            <p>It is under construction</p>
            <a href="/PrahaMetro/">Back</a>
        </div>
    """)


class TeamTemplate(TemplateView):

    template_name = "team_page.html"


class Production(TemplateView):

    template_name = "production.html"


def reception_view(request):
    if request.method == "POST":
        form = UserFormReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = UserFormReg()
    else:
        form = UserFormReg()
        return render(request, "reception.html", context={
            "form": form,
        })
    return HttpResponse("""
    <div>
        <div style="float: center;">
            <p>It isn't working yet!</p>
            <form action="/" method="GET">
                <input type="submit" value="Go Back">
            </form>
        </div>
    </div>
    """)


def enter_view(request):
    if request.method == "GET":
        authen = UserEnter()
        return render(request, "authentication.html", context={
            "AUTH": authen,
        })
    return HttpResponse("""
    <div>
        <div style="float: center;">
            <p>It isn't working yet!</p>
            <form action="/" method="GET">
                <input type="submit" value="Go Back">
            </form>
        </div>
    </div>
    """)

