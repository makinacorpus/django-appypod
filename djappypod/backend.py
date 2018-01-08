from appy.pod.renderer import Renderer
from appy.pod import PodError
import logging
import os
from tempfile import NamedTemporaryFile

from django.template import engines, TemplateDoesNotExist
from django.template.backends.base import BaseEngine
from django.template.context import make_context
from django.template.loaders.app_directories import Loader as BaseLoader
from django.template.engine import Engine, _dirs_undefined

logger = logging.getLogger(__name__)


class Loader(BaseLoader):
    def load_template_source(self, template_name, template_dirs=None):
        for filepath in self.get_template_sources(template_name, template_dirs):
            if filepath.endswith('.odt') and os.path.exists(filepath):
                return filepath, filepath
        raise TemplateDoesNotExist(template_name)


class OdtTemplateError(Exception):
    pass


class OdtTemplates(BaseEngine):
    app_dirname = 'templates'

    def __init__(self, params):
        params = params.copy()
        options = params.pop('OPTIONS').copy()
        super(OdtTemplates, self).__init__(params)
        self.engine = Engine(self.dirs, self.app_dirs, **options)

    def get_template(self, template_name, dirs=_dirs_undefined):
        return Template(self.engine.get_template(template_name, dirs))


class Template(object):
    def __init__(self, path):
        self.path = path

    def render(self, context=None, request=None):
        context_dict = make_context(context, request).flatten()
        output = None
        try:
            with NamedTemporaryFile('rwb', suffix='.odt', delete=False) as f:
                output = f.name
                logger.debug("Render template '%s' to '%s'" % (self.path, output))
                renderer = Renderer(self.path, context_dict, output, overwriteExisting=True)
                renderer.run()
            result = open(output, 'rb').read()
        except (OSError, PodError), e:
            logger.error("Cannot render '%s' : %s" % (self.path, e))
            raise OdtTemplateError(e)
        finally:
            if output and os.path.exists(output):
                os.unlink(output)
        return result
