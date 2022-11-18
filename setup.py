from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='graphs_from_scratch',
    version='0.5.0',
    author='David Castellano ',
    author_email='shudson@anl.gov',
    packages=['graphs_from_scratch'],
    install_requires=required,
)
