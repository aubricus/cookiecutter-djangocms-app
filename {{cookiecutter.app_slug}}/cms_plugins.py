import logging
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from . import models


log = logging.getLogger(__name__)


class {{cookiecutter.app_python_prefix}}PluginAdmin(CMSPluginBase):
    """
    Base CMSPluginBase class.

    The CMSPluginBase name is too easily confused with the backing
    model base class for plugins, CMSPlugin. Since CMSPluginBase
    is, in actuality, an extension of `django.admin.ModelAdmin`
    anyway, we can follow a naming convention that
    makes more sense:

    ```
    class FooPluginAdmin({{cookiecutter.app_python_prefix}}):
        pass
    ```

    """

    pass
