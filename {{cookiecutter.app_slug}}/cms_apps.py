import logging
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from . import apps


log = logging.getLogger(__name__)


@apphook_pool.register()
class {{cookiecutter.app_python_prefix}}AppHook(CMSApp):
    name = "{{cookiecutter.project_name}}: {{cookiecutter.app_name}}"
    app_name = apps.{{cookiecutter.app_python_prefix}}Config.label

    def get_urls(self, page=None, language=None, **kwargs):
        return ["app.{{cookiecutter.app_slug}}.urls", ]
