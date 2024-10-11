# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# TODO(agarwal): optimize if one of the dims == 1.
value_shape = array_ops.shape(value)
v0 = value_shape[0]
v1 = value_shape[1]
value = array_ops.reshape(value, [v0, v1, -1])
value = array_ops.transpose(value, [1, 0, 2])
new_shape = array_ops.concat([[v1, v0], value_shape[2:]], axis=0)
exit(array_ops.reshape(value, new_shape))
