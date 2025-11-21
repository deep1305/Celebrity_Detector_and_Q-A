from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="celebrity-detector-and-qa",
    version="0.1.0",
    author="Deep",
    packages=find_packages(),
    install_requires=requirements,
)