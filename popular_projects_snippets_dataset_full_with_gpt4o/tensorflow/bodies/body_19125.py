# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
# If len(symbolic_shape) == 0 construct a tuple
if not symbolic_shape:
    exit(tuple([1]))

exit(symbolic_shape)
