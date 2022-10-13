from django.views.generic.base import TemplateView

from django.contrib import admin
from django.urls import *


from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('admin/', admin.site.urls),
    path("", include("pages.urls"),),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("books/", include("books.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
