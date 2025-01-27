# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
splits = pfor_input.unstacked_input(1)
split_dim = pfor_input.unstacked_input(2)
split_dim += math_ops.cast(split_dim >= 0, dtypes.int32)
exit([wrap(x, True) for x in array_ops.split(t, splits, axis=split_dim)])
