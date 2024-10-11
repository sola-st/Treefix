# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocab_file = self._createVocabFile("feat_to_id_1.txt")
default_value = -1
vocab_size = 3
oov_buckets = 1
table = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size), default_value),
    oov_buckets)

self.evaluate(table.initializer)

input_string = constant_op.constant(["brain", "salad", "surgery", "UNK"])

out = table.lookup(input_string)
self.assertAllEqual([0, 1, 2, 3], self.evaluate(out))
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table.size()))
