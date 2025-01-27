# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
if isinstance(x, ops.Tensor):
    x = cast(x, result_type)
else:
    x = ops.convert_to_tensor(x, result_type)
exit(x)
