from setuptools import setup, find_packages
from os import path

working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="youtube-downloader-jmbv",
    version="0.0.1",
    author="Juan Manuel Batista Velásquez",
    author_email="juanmabatistav@gmail.com",
    description="Un paquete para descargar vídeos de Youtube a un directorio en concreto",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juanmabv/youtube-downloader-jmbv",
    packages=find_packages(),
    install_requires=[],
)
