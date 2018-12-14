import logging
{% if cookiecutter.django_version == "2.x" %}from django.urls import include, path, re_path{% else %}from django.conf.urls import url{% endif %}
from . import views, apps


log = logging.getLogger(__name__)
app_name = apps.{{cookiecutter.app_python_prefix}}Config.label


urlpatterns = [
    {% if cookiecutter.django_version == "2.x" %}path("", views.IndexView.as_view(), name="index"),{% else %}url(r"^$", views.IndexView.as_view(), name="index"),{% endif %}
]
