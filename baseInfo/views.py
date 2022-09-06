from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, TemplateView
# FormView
from .models import Greeting, MetroShortInfo, Ticket
from django.db.models import Q
from .forms import UserFormReg, AuthUserForm
from django.contrib.auth import logout
# login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from time import sleep
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
    infos = MetroShortInfo.objects.filter(ofiName="Prague Metro")
    verifiq = Ticket.objects.all()
    if request.method == "GET":
        # Table from models.py is going here!
        return render(request, "metro.html", context={
            'INFO' : infos,
            'tickets': verifiq,
        })
    elif request.method == "POST":
        return render(request, "metro.html", context={
            'INFO': infos,
            'tickets': verifiq,
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
            newUser = form.save(commit=False)
            newUser.set_password(form.cleaned_data['password_first'])
            newUser.save()
            return render(request, "done_regist.html", context={})
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


# def enter_view(request):
#     if request.method == "POST":
#         authen = UserEnter(request.POST)
#         if authen.is_valid():
#             # print(authen.cleaned_data)
#             datum = authen.cleaned_data
#             # print(authenticate(email=datum['email'], password=datum['password']))
#             # user = authenticate(email=datum['email'], password=datum['password'])
#             user = authenticate(username=datum['username'])
#             # login_ = request.POST.get('username', '')
#             # pass_ = request.POST.get('pass', '')
#             # print(login_, pass_)
#             # user = authenticate(username=login_, password=pass_)
#             if user is not None:
#                 if user.is_active():
#                     login(request, user)
#                     return HttpResponse("""
#                     <div>
#                         <div style="float: center;">
#                             <p>At this place you would be authenticated. YES, it works,
#                             but now it is under construction. During the next days it
#                             will be corrected. Now you should logout.</p>
#                             <form action="/logout/" method="GET">
#                                 <input type="submit" value="Go Back">
#                             </form>
#                         </div>
#                     </div>
#                     """)
#                 else:
#                     HttpResponse("Disabled account...")
#             else:
#                 return HttpResponse("Invalid login...")
#         else:
#             authen = UserEnter()
#     elif request.method == "GET":
#         authen = UserEnter()
#         return render(request, "authentication.html", context={
#             "AUTH": authen,
#         })
#     # return HttpResponse("""
#     # <div>
#     #     <div style="float: center;">
#     #         <p>It isn't working</p>
#     #         <form action="/" method="GET">
#     #             <input type="submit" value="Go Back">
#     #         </form>
#     #     </div>
#     # </div>
#     # """)

class EnterUserLoginView(LoginView):

    template_name = "authentication.html"
    form_class = AuthUserForm
    success_url = reverse_lazy("Greet")
    def get_success_url(self):
        return self.success_url


def user_out(request):
    logout(request)
    HttpResponse("You have exited.")
    sleep(2)
    return redirect('/')


def loker(request):
    return HttpResponse("""
    <div>
        <div style="float: center;">
            <p>At this place you would be authenticated. YES, it works,
                            but now it is under construction. During the next days it
                            will be corrected. Now you should logout.</p>
            <form action="/logout/" method="GET">
                <input type="submit" value="Go Back">
            </form>
        </div>
    </div>
    """)
