import setuptools

NAME="flipper-zero-in-stock-yet"
VERSION="0.0.1"

with open("requirements.txt", "r") as _file:
    requirements = list(_file.readlines())

setuptools.setup(
    name=NAME,
    version=VERSION,
    author="Hayden Andreyka",
    author_email="haydenandreyka@gmail.com",
    description="Sends an email when the Flipper Zero is in stock",
    install_requires=requirements,
    packages=setuptools.find_packages(),
)
