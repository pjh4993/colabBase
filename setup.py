from distutils.core import setup
from setuptools import find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="colabBase-pjh4993", # Replace with your own username
    version="0.0.1",
    author="junho park",
    author_email="pjh4993@gmail.com",
    description="small machine learning project purposed on colab usage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pjh4993/colabBase",
    packages=find_packages(exclude=("configs", "tests")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
