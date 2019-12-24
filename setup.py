
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="afniRTI-for_usenet", # Replace with your own username
    version="2.7.0",
    author="V. R-singh",
    author_email="for_usenet@yahoo.com",
    description="AFNI real-time interface in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roopchansinghv/afni-real-time-interface-in-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7,<3.0',
    # python_requires='>=3.0',
)

