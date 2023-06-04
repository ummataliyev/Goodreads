from django.urls import path
from django.urls import include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from .views import home_page
from .views import landing_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('books/', include("books.urls")),
    path('home/', home_page, name='home_page'),
    path('users/', include('users.urls'), name="users"),
    path("api/", include("api.urls")),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
