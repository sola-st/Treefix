# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
exit({"dense": math_ops.cast(i, dtype=dtypes.int64),
        "sparse": make_sparse_fn(math_ops.cast(i, dtype=dtypes.int64))})
