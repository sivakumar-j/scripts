#!/usr/bin/env python3.6

import os

# Get the value of 'HOME' environment variable
home = os.environ['HOME'].upper()
print('HOME using environ      :', home)

java_home = os.environ.get('JAVA_HOME')
print('JAVA_HOME using environ :', java_home)

home = os.getenv('MY_RUBY_HOME','HOME').upper()
print('RUBY-HOME using getenv  :', home)

java_home = os.getenv('GEM_HOME','HOME')
print('GEM_HOME using getenv   :', java_home)
