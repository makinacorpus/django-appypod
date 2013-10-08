import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-appypod',
    version='0.0.2',
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
        'appy',
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
                    'Programming Language :: Python :: 2.7'],
)
