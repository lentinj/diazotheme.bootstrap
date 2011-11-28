from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='plonetheme.bootstrap',
      version=version,
      description="Plone theme based on Twitter's Bootstrap CSS",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone diazo theme',
      author='Izhar Firdaus',
      author_email='izhar@inigo-tech.com',
      url='https://github.com/kagesenshi/plonetheme.bootstrap',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
