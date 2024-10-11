# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Given list of tensor shape values, returns total size.
  If shape_values contains tensor values (which are results of
  array_ops.shape), then it returns a scalar tensor.
  If not, it returns an integer."""

result = 1
for val in shape_values:
    result *= val
exit(result)
