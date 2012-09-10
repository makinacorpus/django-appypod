# -*- coding: utf-8 -*-
import codecs
import os
import logging
from tempfile import NamedTemporaryFile

from django.template import Template
from django.template import loader
from django.template.loader import find_template, LoaderOrigin

from appy.pod.renderer import Renderer
from appy.pod import PodError


logger = logging.getLogger(__name__)


class OdtTemplateError(Exception):
    pass


class OdtTemplate(Template):

    def __init__(self, template_string, origin=None, name='<Unknown Template>'):
        self.origin = origin

    def render(self, context):
        contextdict = {}
        for d in context: contextdict.update(**d)
        result = None
        output = None
        try:
            with NamedTemporaryFile('rwb', suffix='.odt', delete=False) as f:
                output = f.name
                logger.debug("Render template '%s' to '%s'" % (self.origin.name, output))
                renderer = Renderer(self.origin.name, contextdict, output, overwriteExisting=True)
                renderer.run()
            result = open(output, 'rb').read()
        except (OSError, PodError), e:
            logger.error("Cannot render '%s' : %s" % (self.filepath, e))
            raise OdtTemplateError(e)
        finally:
            if output:
                os.unlink(output)
        return result

# 
# Code taken from https://github.com/zyegfryed/djangocong-2011
# Author: Sébastien Fievet - http://sebastien-fievet.fr
#
def get_template_from_string(source, origin=None, name=None):
    """
    Returns a compiled Template object for the given template code,
    handling template inheritance recursively.
    """
    if name and name.endswith('.odt'):
        return OdtTemplate('odt', origin, name)
    return Template(source, origin, name)
loader.get_template_from_string = get_template_from_string


def make_origin(display_name, loader, name, dirs):
    # Always return an Origin object, because OdtTemplate need it to render
    # the file.
    return LoaderOrigin(display_name, loader, name, dirs)
loader.make_origin = make_origin


def get_template(template_name):
    """
    Returns a compiled Template object for the given template name,
    handling template inheritance recursively.
    """

    def strict_errors(exception):
        raise exception

    def fake_strict_errors(exception):
        return (u'', -1)

    # Loading hacks
    # Ignore UnicodeError, due to Odt file read
    codecs.register_error('strict', fake_strict_errors)
    # --//--
    template, origin = find_template(template_name)
    # Loading hacks
    codecs.register_error('strict', strict_errors)
    # --//--
    return template
