import logging
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView


log = logging.getLogger(__name__)


class {{cookiecutter.app_python_prefix}}AppBaseView(object):
    """
    Base view class.

    This is an optional base plugin model useful for
    sharing common fields and customizations.
    """

    pass


class IndexView({{cookiecutter.app_python_prefix}}AppBaseView, TemplateView):
    template_name = "{{cookiecutter.app_slug}}/{{cookiecutter.app_slug}}.html"
