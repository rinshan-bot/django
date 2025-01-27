
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('core.urls')),
    path('', HomePage.as_view(), name='home_page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
