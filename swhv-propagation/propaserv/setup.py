from setuptools import setup

kwargs = {'name': 'propaserv',
          'description': 'Solar Propagation Service',
          'long_description': open('README.md').read(),
          'author': 'SWHV ROB',
          'author_email': 'swhv@oma.be',
          'packages': ['propaserv'],
          'scripts': ['bin/propagation_service.py', 'bin/propagation_service.fcgi'],
          'license': 'MIT'}

instllrqrs = ['dill', 'lxml', 'msgpack-python', 'spyne', 'sortedcontainers', 'flup6', 'Werkzeug']
kwargs['install_requires'] = instllrqrs

clssfrs = ["Programming Language :: Python",
           "Programming Language :: Python :: 2.7",
           "Programming Language :: Python :: 3.3",
           "Programming Language :: Python :: Implementation :: CPython",
           "License :: OSI Approved :: MIT License",
           "Development Status :: 5 - Production/Stable",
           "Operating System :: POSIX",
           "Intended Audience :: Science/Research",
           "Intended Audience :: Information Technology",
           "Topic :: Software Development :: Libraries :: Python Modules"]
kwargs['classifiers'] = clssfrs

kwargs['version'] = '0.1'

setup(**kwargs)
