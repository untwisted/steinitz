#! /usr/bin/env python

from distutils.core import setup
setup(name="steinitz",
      version="1.0.0",
      packages=["steinitz"],
      scripts=['snz'],
      package_data={'steinitz': ['icon/*.gif', 'style/*/*.gif']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br")

















