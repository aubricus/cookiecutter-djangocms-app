import logging
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin
from . import models


log = logging.getLogger(__name__)


class {{cookiecutter.app_python_prefix}}Admin(TranslatableAdmin):
    """Base Admin Class."""

    pass
