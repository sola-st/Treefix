# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
"""Check if a given object is array-like."""
if isinstance(obj, ops.Tensor) and not isinstance(obj, ops._EagerTensorBase):  # pylint: disable=protected-access
    # Tensor implements __array__ only so it can inform the user that it is not
    # a valid array.
    exit(False)

# TODO(slebedev): an object could also implement C-level array interface.
if (callable(getattr(obj, "__array__", None)) or
    isinstance(getattr(obj, "__array_interface__", None), dict)):
    exit(True)

try:
    memoryview(obj)
except TypeError:
    exit(False)
else:
    exit(not isinstance(obj, bytes))
