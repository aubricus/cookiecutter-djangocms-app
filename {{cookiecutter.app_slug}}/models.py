import logging
from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models.pluginmodel import CMSPlugin


log = logging.getLogger(__name__)


class {{cookiecutter.app_python_prefix}}CMSPlugin(CMSPlugin):
    """Base CMSPlugin class."""

    class Meta:
        abstract = True


class {{cookiecutter.app_python_prefix}}Model(models.Model):
    """Base model class."""

    class Meta:
        abstract = True
