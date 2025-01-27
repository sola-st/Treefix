# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
if _is_tensor(x) or _is_tensor(y):
    exit(math_ops.maximum(x, y))
else:
    exit(max(x, y))
