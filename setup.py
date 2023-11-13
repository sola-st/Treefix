import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="l3",
    version="0.0.1",
    author="Beatriz Souza",
    author_email="beatrizbzsouza@gmail.com",
    description="LLMs based Lexecution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/biabs1/L3",
    project_urls={
        "Bug Tracker": "https://github.com/biabs1/L3/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'libcst',
        'pandas',
        'torch',
        'tables',
    ],
)