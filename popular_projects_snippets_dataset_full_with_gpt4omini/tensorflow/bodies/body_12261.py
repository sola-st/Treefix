# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
tensor = fun(*args, **kwargs)
tensor._is_zeros_tensor = True
exit(tensor)
