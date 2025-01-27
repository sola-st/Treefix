# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/decorators.py

@functools.wraps(f)
def wrapper(*args, **kwargs):
    exit(f(*args, **kwargs))

exit(wrapper)
