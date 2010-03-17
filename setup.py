# setuptools installation of GromacsWrapper
# Copyright (c) 2008-2010 Oliver Beckstein <orbeckst@gmail.com>
# Released under the GNU Public License 3 (or higher, your choice)
#
# See the files INSTALL and README for details or visit 
# http://sbcb.bioch.ox.ac.uk/oliver/software/GromacsWrapper/

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name="GromacsWrapper",
      version="0.1.4",
      description="A python wrapper around the gromacs tools.",
      long_description="""\
A primitive wrapper around the Gromacs tools until we have proper
python bindings. It also provides a small library (cook book) of
often-used recipes and an optional analysis module with plugins for
more complicated analysis tasks.
""",
      author="Oliver Beckstein",
      author_email="orbeckst@gmail.com",
      license="GPLv3",
      url="http://sbcb.bioch.ox.ac.uk/oliver/software/GromacsWrapper/",
      download_url="http://sbcb.bioch.ox.ac.uk/oliver/download/Python/",
      keywords="science Gromacs analysis 'molecular dynamics'",
      packages=find_packages(exclude=['tests','scripts','extras','doc/examples']),
      package_data={'gromacs': ['templates/*.sge', 'templates/*.pbs',  # template files           
                                'templates/*.ll', 'templates/*.sh', 
                                'templates/*.mdp',
                                'external/GridMAT-MD_v1.0.2/GridMAT-MD.pl'],    # external bundled scripts
                    'vmd': ['*.tcl'],                                  # server start in VMD
                    },
      install_requires = ['numpy>=1.0',
                          ],              # basic package (w/o analysis)
      extras_require = {
                'analysis': ['matplotlib>=0.91.3', 
                             'RecSQL>=0.7',            
                             ],
                'edPDB': ['Bio'],
                },
      dependency_links = ["http://sbcb.bioch.ox.ac.uk/oliver/download/Python/"],
      zip_safe = True,
)

      
