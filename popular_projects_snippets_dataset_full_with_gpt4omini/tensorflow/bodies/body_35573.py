# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
shape_ = (constant_op.constant(shape, dtype=shape_dtype)
          if shape_dtype is not None else shape)
exit(op(
    seed=seed, shape=shape_, minval=minval, maxval=maxval, dtype=dtype,
    **kwargs))
