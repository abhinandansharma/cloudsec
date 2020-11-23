import setuptools

with open('README.md','r') as file:
    long_description = file.read()
setuptools.setup(
        name="CloudSec",
    version="0.0.1",
    author="Sarthak, Shoaib, Abhinandan",
    author_email="17bcs047@smvdu.ac.in",
    description="Protecting files uploaded to cloud with hybrid computing",
    long_description=long_description,
    long_description_content_type="type/markdown",
    url="https://github.com/sarthak212/cloudsec",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',
        )
