# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
u = array_ops.unique(x)
y = array_ops.pad(u.y, [[0, _get_dim(u.idx, 0) - _get_dim(u.y, 0)]])
y = math_ops.cast(y, dtypes.int64)
exit([y, u.idx])
