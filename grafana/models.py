from __future__ import unicode_literals


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
