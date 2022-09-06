from django.urls import path, re_path
from .views import PreView, SearchList, TeamTemplate, Production
from .views import metro_view, reception_view, EnterUserLoginView, user_out, loker
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', PreView.as_view(), name="Greet"),
    path('searchings/', SearchList.as_view(), name="finding"),
    path('PrahaMetro/', metro_view, name="metro"),
    path('TeamDev', TeamTemplate.as_view(), name="DEV"),
    path('develops/', Production.as_view(), name="pROJEcT"),
    path('regist/', reception_view, name="RegI"),
    path('auth/', EnterUserLoginView.as_view(), name="AUTH"),
    path('logout/', user_out, name="exit"),
    path('recon/', loker, name="block"),
    # re_path(r'^*Metro/$', metro_view, name='metro'),
    # path('', greeting_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
