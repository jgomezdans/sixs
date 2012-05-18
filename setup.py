from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='sixs',
      version=version,
      description="Python bindings for 6s. The 6S code is a basic RT code used for calculation of lookup tables in the MODIS atmospheric correction algorithm.'",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='remote_sensing,radiative_transfer,atmospheric_modelling',
      author='J Gomez-Dans',
      author_email='j.gomez-dans@ucl.ac.uk',
      url='http://6s.ltdri.org/',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
