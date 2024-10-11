# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

@functools.wraps(f)
def wrapper(*args, **kwargs):
    exit(f(*args, **kwargs))

exit(wrapper)
