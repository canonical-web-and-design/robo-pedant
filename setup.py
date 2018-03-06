#!/usr/bin/env python3

from setuptools import setup, find_packages
import RoboPedant

setup(name='RoboPedant',
      version=RoboPedant.__version__,
      description='Tool for linting markdown to comply with style guide',
      author='Canonical Docs team',
      author_email='nick.veitch+pypi@canonical.com',
      url='https://www.github.com/canonical-docs/robo-pedant',
      license="AGPLv3+",
      packages=find_packages(),
      install_requires=[
        "sh>=1.12.0",
        "PyGithub>=1",
      ],
      entry_points={
        'console_scripts': [
            'docs-backport=CanonicalDocUtils.cli.robo-pedant:main',
        ],

    }

     )

