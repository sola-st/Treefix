# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
with self.assertRaisesRegex(TypeError, "Invalid `key_dtype`"):
    lookup_ops.IdTableWithHashBuckets(
        None, num_oov_buckets=5, key_dtype=dtypes.float64)
