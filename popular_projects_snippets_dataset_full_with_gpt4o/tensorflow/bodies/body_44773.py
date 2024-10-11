# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/misc.py
exit(array_ops.identity(a) if isinstance(a, ops.Tensor) else a)
