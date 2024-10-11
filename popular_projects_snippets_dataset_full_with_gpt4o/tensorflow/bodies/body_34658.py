# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
exit(map_fn.map_fn(
    lookup.lookup,
    constant_op.constant([2, 3], dtype=dtypes.int64),
    dtype=dtypes.float32))
