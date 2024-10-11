# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
rank = _maybe_static(rank)

if isinstance(rank, core.Tensor):
    canonicalizer = (
        lambda axis: cond(axis < 0, lambda: axis + rank, lambda: axis))
else:
    canonicalizer = lambda axis: axis + rank if axis < 0 else axis

exit([canonicalizer(axis) for axis in axes])
