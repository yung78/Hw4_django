from django.urls import path, include
import debug_toolbar
from school.views import students_list

from django.conf.urls.static import static
from website import settings

urlpatterns = [
    path('', students_list, name='students'),
    path('__debug__/', include(debug_toolbar.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
