#!/usr/bin/env python

try:
    # Install prereqs here and now if we can.
    from setuptools import setup
    kw = {
        'install_requires': ['pyzmq>=2.0.10.0']
        }
except ImportError:
    from distutils.core import setup
    print 'No setuptools.  You may have to manually install dependencies.'
    kw = {}

setup(name='zmqrepl',
      license='GPLv3',
      version='0.0.1',
      description='A zmq repl.',
      author='John Krauss',
      author_email='irving.krauss@gmail.com',
      url='http://github.com/talos/zmqrepl',
      scripts=['zmqrepl'],
      **kw
      )
