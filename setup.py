from setuptools import setup, find_packages

setup(
    name="diffusion-financial-risk",
    version="1.0.0",
    author="Evgeniia Shoshina",
    author_email="1132229532@rudn.ru",
    description="Diffusion Model for Financial Risk Estimation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eashoshina/diffusion-financial-risk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines()
    ],
)