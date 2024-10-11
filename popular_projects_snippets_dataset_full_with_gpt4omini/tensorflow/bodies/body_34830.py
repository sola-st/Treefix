# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
exit(lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.float32,
    default_value=0.0,
    empty_key=-1,
    deleted_key=-2))
