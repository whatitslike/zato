# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# flake8: noqa
from setuptools import setup, find_packages

setup(
      name = 'zato-cli',
      version = '3.0.0+src',

      author = 'Zato Developers',
      author_email = 'info@zato.io',
      url = 'https://zato.io',

      package_dir = {'':'src'},
      packages = find_packages('src'),

      namespace_packages = ['zato'],

      zip_safe = False,
      entry_points = """
      [console_scripts]
      zato = zato.cli.zato_command:main
      """
)
