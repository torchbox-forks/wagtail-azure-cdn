from setuptools import setup, find_packages
from os import path

from wagtail_azure_cdn import __version__


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="wagtail-azure-cdn",
    description="Use Azure CDN with Wagtail",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="MIT",
    include_package_data=True,
    author="Tomasz Knapik",
    author_email="hi@tmkn.org",
    version=__version__,
    packages=find_packages(),
    install_requires=["wagtail"],
    extras_require={
        "testing": ["flake8", "black", "isort", "faker"],
        "cdn": ["azure-mgmt-cdn>=1,<2"],
        "frontdoor": ["azure-mgmt-frontdoor>=1,<2"],
    },
    python_requires=">=3.9",
    url="https://github.com/tm-kn/wagtail-azure-cdn/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.1",
        "Framework :: Django :: 5.2",
        "Framework :: Wagtail",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
