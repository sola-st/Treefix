# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = asarray(a)
if axes is not None:
    axes = asarray(axes)
exit(array_ops.transpose(a=a, perm=axes))
