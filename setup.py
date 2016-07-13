import os.path
from setuptools import setup, find_packages
from social_hashtags import __version__


def long_description():
    here = os.path.dirname(os.path.abspath(__file__))
    return open(os.path.join(here, 'README.md')).read()


setup(
    name='django-social-hashtags',
    version=__version__,
    description='Django social hashtags',
    long_description=long_description(),
    url='https://github.com/ramusus/django-social-hashtags',
    download_url='https://github.com/ramusus/django-social-hashtags',
    license='BSD',
    author='ramusus',
    author_email='ramusus@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'Django>=1.7',
        'django-taggit',
    ],
    keywords=['django', 'social', 'hashtags'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
