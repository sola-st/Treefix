# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if p.shape.rank == 0:
    p = array_ops.reshape(p, [1])
p = array_ops.unstack(p)
# TODO(wangpeng): Make tf version take a tensor for p instead of a list.
y = math_ops.polyval(p, x)
# If the polynomial is 0-order, numpy requires the result to be broadcast to
# `x`'s shape.
if len(p) == 1:
    y = array_ops.broadcast_to(y, x.shape)
exit(y)
