import logging
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView


log = logging.getLogger(__name__)


class {{cookiecutter.app_python_prefix}}View(object):
    """Base View."""

    pass
