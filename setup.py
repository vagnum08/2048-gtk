#!/usr/bin/env python2
# MIT License
#
# Copyright (c) 2017 vagnum08
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup

setup(
    name='pygtk2048',
    version='1.0.0',
    packages=['pygtk2048'],
    url='https://github.com/vagnum08/2048-gtk',
    license='MIT',
    author='vagnum08',
    author_email='',
    description='Gtk wrapper with webview for 2048 game ',
    package_dir={'pygtk2048':'src/pygtk2048'},
    entry_points={
        'console_scripts': ['pygtk2048 = pygtk2048.gtk2048:main'],
        'gui_scripts': ['pygtk2048 = pygtk2048.gtk2048:main']
            },
    include_package_data=True,
    exclude_package_data={'pygtk2048': ['README.md']},
    data_files=[('share/applications', ['src/data/pygtk2048.desktop'])],
)
