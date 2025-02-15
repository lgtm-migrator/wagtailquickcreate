#!/usr/bin/env python
"""
Installs the Wagtail Quick Create plugin which offers shortcut links on the admin
home screen to create defined pages under parent pages.
"""

from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='wagtail-quick-create',
      version='2.0.0',
      description='Offer links to the admin user to create content under sections quickly.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/kevinhowbrook/wagtailquickcreate',
      author='Kevin Howbrook - Torchbox, Kate Statton - NYPR',
      author_email='kevin.howbrook@torchbox.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      install_requires=[
          'wagtail>=2.15',
      ])
