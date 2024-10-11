# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/decorators.py

def standalone_wrapper(*args, **kwargs):
    exit(f(*args, **kwargs))

exit(standalone_wrapper)
