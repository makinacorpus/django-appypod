*django-appypod* allows to serve OpenDocument Text files (*.odt*) from templates
and contexts, using `Appy POD <appyframework.org>`_ framework.

=======
INSTALL
=======

::

    pip install django-appypod


=====
USAGE
=====

In settings, add OdtTemplates template backend before DjangoTemplates one :

::

    TEMPLATES = [
        {
            'BACKEND': 'djappypod.backend.OdtTemplates',
        },
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            ...
        },
    ]



Using class-based generic views :

::

    from django.view.generic.detail import DetailView
    
    from djappypod.response import OdtTemplateResponse
    
    class YourDocument(DetailView):
        response_class = OdtTemplateResponse
        template_name = "your/template.odt"


Using classic views functions :

::

    def your_view(request):
        response = OdtTemplateResponse(request, "your/template.odt", {
            'title': 'Simple as hello ;)'
        })
        response.render()
        return response


Follow instructions in `Appy POD documentation <http://appyframework.org/podWritingTemplates.html>`_ 
for designing your OpenDocument templates.

=======
AUTHORS
=======

    * Mathieu Leplatre <mathieu.leplatre@makina-corpus.com>
    * Gaël Utard <gael.utard@makina-corpus.com>
    * Template loading based on Sébastien Fievet's presentation at DjangoCong 2011

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

=======
LICENSE
=======

    * Lesser GNU Public License
