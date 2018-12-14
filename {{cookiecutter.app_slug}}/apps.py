import logging
from django.apps import AppConfig


log = logging.getLogger(__name__)


class {{cookiecutter.app_python_prefix}}Config(AppConfig):
    name = "app.{{cookiecutter.app_slug}}"
    label = "app_{{cookiecutter.app_slug}}"
    verbose_name = "{{cookiecutter.app_name}}"

    def ready(self):
        pass
