#!/usr/bin/env python
 
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
 
d = generate_distutils_setup()

d['packages'] = ['dslam_bag']
d['package_dir'] = {'': 'python'}
d['scripts'] = ['scripts/dslam_bag']
 
setup(**d)

