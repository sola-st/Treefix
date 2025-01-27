# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
dtype = dtypes.as_dtype(dtype)
exit(random_ops.random_uniform(shape=[2], dtype=dtype, maxval=dtype.max))
