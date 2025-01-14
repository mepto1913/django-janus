from setuptools import setup, find_packages
from janus import __version__


setup(
    name="django-janus",
    version='.'.join(str(x) for x in __version__),
    license="BSD",
    description="Janus is a Single sign-on (SSO) system based on django.",
    author="Daniel Leinfelder",
    author_email="daniel@smart-lgt.com",
    url="https://github.com/smartlgt/django-janus",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=2.0,<4.0",
        "django-oauth-toolkit==1.3.2",
        "django-cors-middleware>=1.5.0",
        "django_python3_ldap>=0.11.3,<0.15.0",
        "django-allauth>=0.42.0",
        "django-fakeinline>=0.1.1",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Framework :: Django",
    ]
)
