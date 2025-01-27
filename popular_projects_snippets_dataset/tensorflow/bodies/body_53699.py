# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if callable(condition):
    skip = condition()
else:
    skip = condition
if not skip:
    exit(fn(*args, **kwargs))
