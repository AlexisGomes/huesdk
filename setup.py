import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='huesdk',
    version='1.6',
    packages=setuptools.find_packages(),
    author="Gomes Alexis",
    author_email="alexis.gomes19@gmail.com",
    description="A python SDK for the Philips hue API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexisGomes/huesdk",
    install_requires=[
        "requests",
        "zeroconf"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
