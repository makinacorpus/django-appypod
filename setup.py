import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-appypod',
    version='2.0.6.dev0',
    author='Mathieu Leplatre',
    author_email='mathieu.leplatre@makina-corpus.com',
    url='https://github.com/makinacorpus/django-appypod/',
    download_url='http://pypi.python.org/pypi/django-appypod/',
    description='Render OpenDocument files from templates, using Appy POD',
    long_description=open(os.path.join(here, 'README.rst')).read() + '\n\n' + 
                     open(os.path.join(here, 'CHANGES')).read(),
    license='LPGL, see LICENSE file.',
    install_requires=[
        'Django',
        'appy-python-3@git+ssh://git@github.com/GeotrekCE/appy-python-3@b3f31e8c0c1e1dd774a526d3c1e0a5b48bdb43d7',
    ],
    packages=find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers  = ['Topic :: Utilities', 
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Development Status :: 5 - Production/Stable',
                    'Programming Language :: Python :: 3.5'],
)
