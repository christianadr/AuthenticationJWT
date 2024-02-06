from django.urls import path, re_path, include
from django.views.generic import TemplateView 


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# handles catch-all route and renders the matched template
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))] 