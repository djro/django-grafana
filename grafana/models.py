from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from jsonfield import JSONField


class CreatedModelMixin(object):
    created = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(CreatedModelMixin, self).__init__(*args, **kwargs)


class UpdatedModelMixin(object):
    updated = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(UpdatedModelMixin, self).__init__(*args, **kwargs)


class ChangedModelMixin(CreatedModelMixin, UpdatedModelMixin):
    pass


class Dashboard(ChangedModelMixin, models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    version = models.IntegerField()
    data = JSONField()
    organization = models.ForeignKey("Organization")
    # Grafana stores all data related to a dashboard (panels, tags etc.)
    # in JSON. Maybe I'll try to change this in something more rational.

    class Meta:
        verbose_name = "Dashboard"
        verbose_name_plural = "Dashboards"

    def __str__(self):
        return self.slug


class Organization(ChangedModelMixin, models.Model):
    name = models.CharField(max_length=256)
    version = models.IntegerField()
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="UserInOrganization",
        through_fields=("organization", "user")
        )

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name


class UserInOrganization(ChangedModelMixin, models.Model):
    organization = models.ForeignKey("Organization")
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    role = models.ForeignKey("UserRole")

    class Meta:
        verbose_name = "UserInOrganization"
        verbose_name_plural = "UsersInOrganizations"
