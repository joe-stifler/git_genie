from setuptools import setup, find_packages

setup(
    name="git_genie",
    version="0.1.0",
    author="Joe",
    author_email="joseribeiro1017@gmail.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["git_genie=git_genie.__init__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="A simple crawler.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
