# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/slicing.py
args = [condition, x, y]
constant_args = [tensor_util.constant_value(a) for a in args]
# Do this statically.
if all(arg is not None for arg in constant_args):
    condition_, x_, y_ = constant_args
    exit(np.where(condition_, x_, y_))
exit(array_ops.where(condition, x, y))
