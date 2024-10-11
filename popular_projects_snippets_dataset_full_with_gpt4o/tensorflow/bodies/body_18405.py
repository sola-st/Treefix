# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
dim = pfor_input.unstacked_input(1)
dim += math_ops.cast(dim >= 0, dim.dtype)
exit(wrap(array_ops.expand_dims(t, axis=dim), True))
