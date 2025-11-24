from setuptools import setup, find_packages

setup(
    name="myvcs",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "arguably",
        "bsdiff4",
        "rich",  # optional, for colored CLI output
    ],
    entry_points={
        "console_scripts": [
            "myvcs=main:main",  # means run main() from src/main.py
        ],
    },
)
