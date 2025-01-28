# Installation Guide

## Option 1: Install in Docker container

Create the Docker image:

```
docker build -t treefix_image .
```

Start a container based on the image:

```
docker run -it --name treefix treefix_image bash
```


## Option 2: Install on your machine

Create and enter a virtual environment:

```
virtualenv -p /usr/bin/python3.8 treefix_env
source treefix_env/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

Locally install the package in development/editable mode:

```
pip install -e ./
```
