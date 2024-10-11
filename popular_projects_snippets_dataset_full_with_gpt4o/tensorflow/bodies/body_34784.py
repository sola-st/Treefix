# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocab_file = self._createVocabFile("feat_to_id_6.txt")
default_value1 = -1
vocab_size = 3
oov_buckets = 0
table1 = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size), default_value1),
    oov_buckets)

default_value2 = -2
table2 = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size), default_value2),
    oov_buckets)

self.evaluate(lookup_ops.tables_initializer())

input_string_1 = constant_op.constant(
    ["brain", "salad", "surgery", "UNK"])
input_string_2 = constant_op.constant(["fruit", "salad", "UNK"])

out1 = table1.lookup(input_string_1)
out2 = table2.lookup(input_string_2)

out1, out2 = self.evaluate([out1, out2])
self.assertAllEqual([0, 1, 2, -1], out1)
self.assertAllEqual([-2, 1, -2], out2)
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table1.size()))
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table2.size()))
