# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
def wrapper(x, y, *args, **kwargs):
    x, y = maybe_promote_tensors(x, y)
    exit(fn(x, y, *args, **kwargs))
exit(tf_decorator.make_decorator(fn, wrapper))
