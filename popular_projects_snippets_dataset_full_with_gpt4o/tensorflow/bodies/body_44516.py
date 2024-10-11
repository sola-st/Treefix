# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if step is not UNSPECIFIED:
    exit(range(start_or_stop, stop, step))
if stop is not UNSPECIFIED:
    exit(range(start_or_stop, stop))
exit(range(start_or_stop))
