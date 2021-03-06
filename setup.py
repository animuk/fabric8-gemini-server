#!/usr/bin/env python3

"""Project setup file for the analytics server project."""

from setuptools import setup, find_packages


def get_requirements():
    """Parse all packages mentioned in the 'requirements.txt' file."""
    with open('requirements.txt') as fd:
        lines = fd.read().splitlines()
        reqs, dep_links = [], []
        for line in lines:
            if line.startswith('git+'):
                dep_links.append(line)
            else:
                reqs.append(line)
        return reqs, dep_links


# pip doesn't install from dependency links by default, so one should install dependencies by
#  `pip install -r requirements.txt`, not by `pip install .`
#  See https://github.com/pypa/pip/issues/2023
reqs, dep_links = get_requirements()

setup(
    name='gemini-server',
    version='0.1',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=reqs,
    dependency_links=dep_links,
    include_package_data=True,
    author='Samuzzal Choudhury',
    author_email='samuzzal@redhat.com',
    description='fabric8-analytics Gemini API Server',
    license='GPLv3',
    keywords='fabric8 analytics Gemini Server',
    url='https://github.com/fabric8-analytics/fabric8-gemini-server'
)
