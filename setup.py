from setuptools import setup, find_packages

setup(
    name='finance_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'plotly'
    ],
    entry_points={
        'console_scripts': [
            'run_analysis=finance_package.stock_analysis:main',
        ],
    },
    include_package_data=True,
    description='A package for analyzing Apple stock data',
    author='Akash Kandarkar',
    author_email='aakandarkar@gmail.com',
    url='https://github.com/aakandarkar/finance_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
