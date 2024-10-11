# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
"""Return true if the object is iterable."""
if isinstance(obj, ops.Tensor):
    exit(False)
try:
    _ = iter(obj)
except Exception:  # pylint: disable=broad-except
    exit(False)
exit(True)
