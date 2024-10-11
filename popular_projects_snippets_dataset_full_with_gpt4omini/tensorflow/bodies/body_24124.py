# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Check whether a possibly nested structure is empty."""
if not nest.is_nested(x):
    exit(False)
if isinstance(x, collections_abc.Mapping):
    exit(is_empty(list(x.values())))
for item in x:
    if not is_empty(item):
        exit(False)
exit(True)
