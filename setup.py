#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Aurelie Albert",
    author_email='aurelie.albert@univ-grenoble-alpes.fr',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Generate pseudo- ARGO floats profiles in eNATL60 simulations",
    entry_points={
        'console_scripts': [
            'pseudo_argo_floats_in_enatl60=pseudo_argo_floats_in_enatl60.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pseudo_argo_floats_in_enatl60',
    name='pseudo_argo_floats_in_enatl60',
    packages=find_packages(include=['pseudo_argo_floats_in_enatl60', 'pseudo_argo_floats_in_enatl60.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/auraoupa/pseudo_argo_floats_in_enatl60',
    version='0.1.0',
    zip_safe=False,
)
