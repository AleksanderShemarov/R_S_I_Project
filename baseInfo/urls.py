from django.urls import path, re_path
from .views import PreView, SearchList
from .views import metro_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', PreView.as_view(), name="Greet"),
    path('searchings/', SearchList.as_view(), name="finding"),
    path('PrahaMetro/', metro_view, name="metro"),
    # re_path(r'^*Metro/$', metro_view, name='metro'),
    # path('', greeting_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
