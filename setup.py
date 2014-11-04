#! /usr/bin/env python

from distutils.core import setup
setup(name="vy",
      version="0.1",
      packages=["steinitz"],
      scripts=['snz'],
      package_data={'steinitz': ['icon/*.gif', 'style/*/*.gif']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br")
















