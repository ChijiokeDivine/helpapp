
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import re_path as url
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from core.sitemaps import StaticSitemap, BlogSitemap
from django.contrib.sitemaps.views import sitemap
sitemaps = {
    'static': StaticSitemap,
    'Blog': BlogSitemap,
}

context = {
    'sitemaps': sitemaps
}

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path("helpappafrica/admin/", admin.site.urls),
    path("", include('core.urls')),
    path('sitemap.xml/', sitemap, context, name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



handler400 = 'core.views.error_400'
handler404 = 'core.views.error_404'
handler403 = 'core.views.error_403'
handler500 = 'core.views.error_500'