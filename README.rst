*django-appypod* allows to serve OpenDocument Text files (*.odt*) from templates
and contexts, using `Appy POD <appyframework.org>`_ framework.

=======
INSTALL
=======

::

    pip install django-appypod

Requires ``appy.pod`` in python path. It has to be deployed manually, 
since it does not come with any ``setup.py``. 

A possibility is to create a ``.pth`` file in your *site-packages* folder,
or modify ``sys.path`` on-the-fly.

Alternatively, if you use *buildout*, a few lines do the job :

::

    [buildout]
    extra-paths += src/appy-archive/
    parts += download-appy-archive

    [download-appy-archive]
    recipe = hexagonit.recipe.download
    url = https://launchpad.net/appy/0.8/0.8.1/+download/appy-0.8.1.zip
    destination = src/appy-archive/



=====
USAGE
=====

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
    * Template loading based on Sébastien Fievet's presentation at DjangoCong 2011

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

=======
LICENSE
=======

    * Lesser GNU Public License
