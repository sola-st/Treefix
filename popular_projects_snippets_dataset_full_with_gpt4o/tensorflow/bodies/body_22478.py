# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
exit(isinstance(v, ops.Tensor) and v.op.type in _VARIABLE_OPS)
