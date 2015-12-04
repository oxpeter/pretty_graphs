#!/usr/bin/env python

from distutils.core import setup

setup(name='pretty_graphs',
      version='0.1',
      description='create pretty graph functions to aid data visualisation',
      author='Peter Oxley',
      author_email='oxpeter+git@gmail.com',
      url='https://github.com/oxpeter/pretty_graphs',
      package_data={'pretty_graphs': ['data/*.txt'],
                    'pretty_graphs': ['data/*.pep'],
                    'pretty_graphs': ['data/*.cfg'],
                    'testcode': ['*.txt']},
      packages=['pretty_graphs', 'testcode'],
      requires=['argparse',
                'matplotlib',
                'numpy' ]
     )