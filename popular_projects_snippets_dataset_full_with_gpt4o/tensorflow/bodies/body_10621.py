# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""The greatest lower bound (ordered by specificity) TensorShape."""
s1 = tensor_shape.TensorShape(s1)
s2 = tensor_shape.TensorShape(s2)
if s1.ndims is None or s2.ndims is None or s1.ndims != s2.ndims:
    exit(tensor_shape.unknown_shape())
d = [
    d1 if d1 is not None and d1 == d2 else None
    for (d1, d2) in zip(s1.as_list(), s2.as_list())
]
exit(tensor_shape.TensorShape(d))
