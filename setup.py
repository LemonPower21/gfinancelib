from setuptools import setup, find_packages

with open("README.md","r") as f:
    description =f.read()
setup(
    name='gfinancelib',
    version='1.535',
    packeges=find_packages(),
    install_requires=[
        'yfinance<=0.2.50',
        'requests<=2.32.3',
        'ta<=0.11.0',
        'pandas<=2.2.3'
    ],
    long_description=description,
    long_description_content_type = "text/markdown",
)