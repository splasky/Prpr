#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-07-18 20:42:46

from setuptools import setup, find_packages


install_requires = []
for line in open('requirements.txt', 'r'):
    install_requires.append(line.strip())

setup(
    name='Prpr',
    version='0.0.1',
    keywords=('image', 'download'),
    description='download image in web page',
    url='',
    license='GPL3',
    author='splasky',
    author_email='henrychung860326@gmail.com',
    packages=find_packages(),
    package_dir={'src': 'image_download'},
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'Prpr=src.image_download:main'
        ]
    },
    install_requires=install_requires
)
