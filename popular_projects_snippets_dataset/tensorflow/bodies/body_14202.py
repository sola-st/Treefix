# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
if a is None:
    exit(b)
if b is None:
    exit(a)
exit(a._merge_with(b))  # pylint: disable=protected-access
