# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
try:
    exit(reg.lookup(obj))
except LookupError:
    pass
exit(None)
