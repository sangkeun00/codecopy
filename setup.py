from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["pyperclip"],
    entry_points={
        'console_scripts': [
            'codecopy = src.main:main',
        ],
    },
)
