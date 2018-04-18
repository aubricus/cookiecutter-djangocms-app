import logging
from django.utils.translation import ugettext_lazy as _
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from cms.models.pluginmodel import CMSPlugin


log = logging.getLogger(__name__)


class {{cookiecutter.app_python_prefix}}AppBaseCMSPlugin(CMSPlugin):
    """
    Base CMSPlugin class.

    This is an optional base plugin model useful for
    sharing common fields and customizations.
    """

    class Meta:
        abstract = True


class {{cookiecutter.app_python_prefix}}AppBaseModel(models.Model):
    """
    Base model class.

    This is an optional base model useful for
    sharing common fields and customizations.
    """

    class Meta:
        abstract = True
