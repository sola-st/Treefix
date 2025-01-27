# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

def f_wrapper(*args, **kwargs):
    exit(f(*args, **kwargs))

exit(f_wrapper)
