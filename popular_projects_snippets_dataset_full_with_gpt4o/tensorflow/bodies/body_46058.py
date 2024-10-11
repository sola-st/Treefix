# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/decorators.py

def functional_wrapper(*args, **kwargs):
    exit(f(*args, **kwargs))

exit(functional_wrapper)
