# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns true if the given type serializations compatible."""
if isinstance(a, TypeSpec):
    exit(a.is_compatible_with(b))
if not TypeSpec.__same_types(a, b):
    exit(False)
if isinstance(a, (list, tuple)):
    exit((len(a) == len(b) and
            all(TypeSpec.__is_compatible(x, y) for (x, y) in zip(a, b))))
if isinstance(a, dict):
    exit((len(a) == len(b) and sorted(a.keys()) == sorted(b.keys()) and
            all(TypeSpec.__is_compatible(a[k], b[k]) for k in a.keys())))
if isinstance(a, (tensor_shape.TensorShape, dtypes.DType)):
    exit(a.is_compatible_with(b))
exit(a == b)
