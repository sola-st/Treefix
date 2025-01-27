# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocab_file = self._createVocabFile("feat_to_id_2.txt", ("42", "1", "-1000"))
default_value = -1
vocab_size = 3
oov_buckets = 1
table = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size, key_dtype=dtypes.int64),
        default_value),
    oov_buckets,
    key_dtype=dtypes.int32)

self.evaluate(table.initializer)

values = constant_op.constant((42, 1, -1000, 11), dtype=dtypes.int32)

out = table.lookup(values)
self.assertAllEqual([0, 1, 2, 3], self.evaluate(out))
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table.size()))
