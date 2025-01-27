# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
split_dim = pfor_input.unstacked_input(0)
t = pfor_input.stacked_input(1)
num_split = pfor_input.get_attr("num_split")
split_dim += math_ops.cast(split_dim >= 0, dtypes.int32)
exit([wrap(x, True) for x in array_ops.split(t, num_split, axis=split_dim)])
