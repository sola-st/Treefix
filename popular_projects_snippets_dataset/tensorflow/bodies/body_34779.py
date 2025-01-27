# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
oov_buckets = 5

# Set a table that only uses hash buckets, for each input value returns
# an id calculated by fingerprint("input") mod oov_buckets.
table = lookup_ops.IdTableWithHashBuckets(
    None, oov_buckets, key_dtype=dtypes.int32)
self.evaluate(table.initializer)

input_string = constant_op.constant([42, 1, -1000], dtype=dtypes.int32)

out = table.lookup(input_string)
self.assertAllEqual(
    [
        1,  # fingerprint("42") mod 5.
        4,  # fingerprint("1") mod 5.
        2  # fingerprint("-1000") mod 5
    ],
    self.evaluate(out))
self.assertEqual(oov_buckets, self.evaluate(table.size()))
