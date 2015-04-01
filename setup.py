import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yoloimport",
    version = "0.0.1",
    author = "Cody Soyland",
    author_email = "codysoyland@gmail.com",
    description = "Never see another ImportError",
    license = "BSD",
    url = "https://github.com/codysoyland/yoloimport",
    py_modules=['yoloimport'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
)
