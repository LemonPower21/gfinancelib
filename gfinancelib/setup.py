from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='gfinancelib',  # Name of the package
    version='2.0',  # Version number
    packages=find_packages(),  # Automatically discover all packages
    install_requires=[  # List of dependencies
        'yfinance>=0.1.63',  # To fetch financial data
        'ta>=0.11.0',  # For technical analysis (RSI, EMA, etc.)
        'requests>=2.28.0',  # For HTTP requests if needed (though not used explicitly in code)
        'pandas>=1.5.0',  # Required by yfinance and for DataFrame operations
        'numpy>=1.23.0',  # For numerical operations (though indirectly used by pandas/ta)
        'smtplib',  # Part of Python Standard Library (no need to include in install_requires)
        'email',  # Part of Python Standard Library (no need to include in install_requires)
    ],
    long_description=description,  # Content of the README for long description
    long_description_content_type="text/markdown",  # Format of the long description
    classifiers=[  # Additional metadata (optional)
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python version requirement
)
