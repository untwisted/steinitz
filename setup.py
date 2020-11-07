
from distutils.core import setup
setup(name="steinitz",
      version="2.1.0",
      packages=["steinitz"],
      scripts=['snz'],
      package_data={'steinitz': ['icon/*.gif', 'style/*/*.gif']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br",
      url='https://github.com/iogf/steinitz',
      download_url='https://github.com/iogf/steinitz/releases',
      keywords=['chess', 'fics', 'interface', 'stockfish', 'untwisted'],
      classifiers=[],
      description="A chess interface to fics built on top of untwisted")





















