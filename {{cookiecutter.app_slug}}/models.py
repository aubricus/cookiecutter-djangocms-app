import logging
from django.db import models
{% if cookiecutter.is_djangocms_app.lower() == "y" %}from cms.models.pluginmodel import CMSPlugin{% endif %}


log = logging.getLogger(__name__)
