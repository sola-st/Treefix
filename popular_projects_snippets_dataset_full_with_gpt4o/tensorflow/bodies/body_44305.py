# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
rand_rank = random_ops.random_uniform(
    shape=(), minval=3, maxval=4, dtype=dtypes.int32)
rand_shape = array_ops.ones([rand_rank], dtype=dtypes.int32)
exit(array_ops.fill(rand_shape, value))
