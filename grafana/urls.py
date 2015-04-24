from django.conf.urls import patterns, url, include
import api as api_views


dashboards_urls = patterns(
    '',
    url(r'^home/$', api_views.home_dashboard, name='home_dashboard'))


urlpatterns = patterns(
    '',
    url(r'^dashboards/', include(dashboards_urls)),
    )
