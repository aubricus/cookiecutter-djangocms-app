import logging
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView


log = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = "{{cookiecutter.app_slug}}/{{cookiecutter.app_slug}}.html"
