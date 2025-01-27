# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
if elements is None:
    exit(frozenset())
elif isinstance(elements, str):
    exit(frozenset((elements,)))
else:
    exit(frozenset(elements))
