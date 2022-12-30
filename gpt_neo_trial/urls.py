from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.GENERATED_WORKBOOKS_URL, document_root=settings.GENERATED_WORKBOOKS_ROOT) \
    + static(settings.ANNOTATED_REQS_DOCS_URL, document_root=settings.ANNOTATED_REQS_DOCS_ROOT)