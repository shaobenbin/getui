#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" create at 5/5/16 """

__author__ = 'binbin'

from distutils.core import setup

setup(name='getui',
      version='4.0.1.0',
      description='Python Distribution Utilities',
      author='shaobenbin',
      author_email='shaobenbin@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['getui', 'getui.google','getui.igetui','getui.payload','getui.protobuf','getui.google.protobuf','getui.google.protobuf.compiler','getui.google.protobuf.internal','getui.google.protobuf.pyext','getui.igetui.template','getui.igetui.utils'],
     )
