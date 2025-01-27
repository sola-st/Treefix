# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
rand_vect = math_ops.range(
    random_ops.random_uniform(
        shape=(), minval=2, maxval=3, dtype=dtypes.int32))
exit(array_ops.expand_dims_v2(rand_vect, 0) < 0)
