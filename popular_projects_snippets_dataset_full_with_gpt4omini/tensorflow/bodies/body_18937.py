# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py

def _decorator(func):
    func.__doc__ = doc
    exit(func)

exit(_decorator)
