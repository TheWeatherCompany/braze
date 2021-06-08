from setuptools import find_packages
from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='braze-sdk',
    version='1.0.0',
    description='Braze Python 3 SDK.',
    packages=find_packages(),
    keywords=(
        'Braze API'),
    install_requires=[],
    url='https://github.com/paulokuong/braze',
    author='Paulo Kuong',
    license='MIT',
    tests_require=['pytest', 'pytest-cov'],
    long_description=long_description,
    include_package_data=True,
    zip_safe=False,
)
