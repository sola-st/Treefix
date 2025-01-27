# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocab_file = self._createVocabFile("feat_to_id_5.txt")
default_value = -1
vocab_size = 3
oov_buckets = 1
table1 = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size), default_value), oov_buckets)

self.evaluate(table1.initializer)

input_string_1 = constant_op.constant(["brain", "salad", "surgery", "UNK"])

out1 = table1.lookup(input_string_1)

self.assertAllEqual([0, 1, 2, 3], self.evaluate(out1))
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table1.size()))

default_value = -1
vocab_size = 3
oov_buckets = 1

# Underlying lookup table already initialized in previous session.
# No need to call self.evaluate(table2.initializer)
table2 = lookup_ops.IdTableWithHashBuckets(
    lookup_ops.StaticHashTable(
        lookup_ops.TextFileIdTableInitializer(
            vocab_file, vocab_size=vocab_size), default_value), oov_buckets)

input_string_2 = constant_op.constant(["fruit", "salad", "UNK"])

out2 = table2.lookup(input_string_2)

self.assertAllEqual([3, 1, 3], self.evaluate(out2))
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table2.size()))
