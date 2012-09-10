from django.template.response import TemplateResponse

from .odt import get_template


class OdtTemplateResponse(TemplateResponse):
    def __init__(self, *args, **kwargs):
        kwargs['content_type'] = 'application/vnd.oasis.opendocument.text'
        super(OdtTemplateResponse, self).__init__(*args, **kwargs)

    def resolve_template(self, template):
        "Accepts a template object, path-to-template or list of paths"
        if isinstance(template, (list, tuple)):
            return get_template(template[0])  # TODO: this is rough
        elif isinstance(template, basestring):
            return get_template(template)
        else:
            return template
