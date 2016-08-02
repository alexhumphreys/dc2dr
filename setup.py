#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pytsort==0.1.2',
    'PyYAML==3.11'
]

test_requirements = [
    'pytest==2.9.2'
]

setup(
    name='dc2dr',
    version='0.3.0',
    description="Convert Docker Compose to Docker Run Commands",
    long_description=readme + '\n\n' + history,
    author="Alex Humphreys",
    author_email='humphreys.a@gmail.com',
    url='https://github.com/alexhumphreys/dc2dr',
    packages=[
        'dc2dr',
    ],
    package_dir={'dc2dr':
                 'dc2dr'},
    entry_points={
        'console_scripts': [
            'dc2dr=dc2dr.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='dc2dr',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
