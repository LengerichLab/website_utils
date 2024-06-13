"""
Setup for installing this repo locally.
Should be modified for your repo by listing included packages.
"""

import setuptools
from setuptools import find_packages

setuptools.setup(name='website_utils',
      packages=find_packages(),
      version='0.0.0',
      install_requires=[
          'bibtexparser',
          'pandas',
          'wordcloud',
          'matplotlib',
      ],
         test_suite='tests',

)
