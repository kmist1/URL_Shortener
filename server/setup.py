from setuptools import setup, find_packages

setup(
    name='server',
    version='0.1.0',
    packages=find_packages(include=['flask_app1', 'flask_app1.*']),
    install_requires=['flask == 1.1.2','pymongo','flask_mongoengine']
)