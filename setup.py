from distutils.core import setup
import os.path
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyshield",
    packages=setuptools.find_packages(),
    version="0.0.1",
    license="MIT",
    description="Hard Obfuscate Tool For Python",
    author="0xe2d0",
    url="https://github.com/davidteather/python-obfuscator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/davidteather/python-obfuscator/tarball/master",
    keywords=["obfuscator","python-obfuscate","pyshield","python code obfuscate"],
    install_requires=["regex","rich"],
   classifiers=[
        "Development Status :: 1 - Tests",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["pyobfuscate=python_obfuscator.cli:cli"]},
)
