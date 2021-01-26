import os

from setuptools import setup


setup(
    name="pytest-test-marker",
    description=('Pytest plugin used to mark tests by reading manifest files'),
    url='https://github.com/tonydelanuez/pytest-test-marker',
    author='Tony De La Nuez',
    author_email='tony.delanuez@gmail.com',
    packages=['pytest_test_marker'],
    version='0.0.0',
    install_requires=['pytest>=2.5', 'PyYAML==5.4.1'],
    classifiers=['Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Testing',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                ]
)