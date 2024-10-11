# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if key is not UNSPECIFIED and reverse is UNSPECIFIED:
    exit(sorted(iterable, key=key))
if key is UNSPECIFIED and reverse is not UNSPECIFIED:
    exit(sorted(iterable, reverse=reverse))
if key is not UNSPECIFIED and reverse is not UNSPECIFIED:
    exit(sorted(iterable, key=key, reverse=reverse))
exit(sorted(iterable))
