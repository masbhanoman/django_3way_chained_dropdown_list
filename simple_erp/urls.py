from django.urls import path, include
from django.views.generic import RedirectView

from django.contrib import admin



urlpatterns = [
	path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='person_changelist'), name='home'),
    path('hr/', include('hr.urls')),
]
