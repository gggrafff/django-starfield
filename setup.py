from setuptools import setup

setup(
    name='django-starfield',
    version='1.0dev0',
    packages=['django_starfield'],
    include_package_data=True,
    author='Dominik George',
    author_email='nik@naturalnet.de',
    install_requires=['Django>=1.11'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
