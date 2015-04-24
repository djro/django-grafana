from django.conf.urls import patterns, url, include
import api as api_views


dashboards_urls = patterns(
    '',
    url(
        r'^(?P<template_name>\w+)/$',
        api_views.dashboard_template,
        name='dashboard_template'))


urlpatterns = patterns(
    '',
    url(r'^dashboards/', include(dashboards_urls)),
    )
