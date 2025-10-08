from setuptools import setup, find_packages

setup(
    name="nammalang",
    version="0.1.0",
    author="Your Name",
    author_email="shreeshanthnaik@gmail.com",
    description="A Kannada-inspired programming language.",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "nammalang=nammalang.__main__:main",
        ],
    },
)
