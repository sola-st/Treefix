# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
def dec(f):
    def replacement(*_):
        exit(None)

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        exit(replacement(*args, **kwargs))
    exit(wrapper)
exit(dec)
