from rest_framework import serializers as rest_serializers
import datetime


class ConfigurableFieldsMixin(object):
    """
    This mixin allows to change serializable fields in run time
    (when creating the instance).
    Just pass a list/tuple with names of fields that you want to
    serialize (as the `field` argument).
    """
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(ConfigurableFieldsMixin, self).__init__(*args, **kwargs)
        if fields and isinstance(fields, (list, tuple)):
            new_fields = set(fields)
            existing_fields = set(self.fields.keys())
            for field in existing_fields - new_fields:
                self.fields.pop(field)


class DashboardMetaSerializer(
        ConfigurableFieldsMixin,
        rest_serializers.Serializer):
    isStarred = rest_serializers.BooleanField(default=False)
    isHome = rest_serializers.BooleanField(default=False)
    isSnapshot = rest_serializers.BooleanField(default=False)
    slug = rest_serializers.SlugField()
    expires = rest_serializers.DateTimeField(
        format='iso-8601',
        default=datetime.datetime.min)
    created = rest_serializers.DateTimeField(
        format='iso-8601',
        default=datetime.datetime.min)


class DashboardDataSerializer(rest_serializers.DictField):
    pass


class DashboardSerializer(rest_serializers.Serializer):
    model = DashboardDataSerializer()
    meta = DashboardMetaSerializer()
