# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocab_file = self._createVocabFile("feat_to_id_4.txt")
default_value = -1
vocab_size = 3
oov_buckets = 3

vocab_table = lookup_ops.StaticHashTable(
    lookup_ops.TextFileIdTableInitializer(
        vocab_file, vocab_size=vocab_size), default_value)
table1 = lookup_ops.IdTableWithHashBuckets(
    vocab_table,
    oov_buckets,
    hasher_spec=lookup_ops.FastHashSpec,
    name="table1")

table2 = lookup_ops.IdTableWithHashBuckets(
    vocab_table,
    oov_buckets,
    hasher_spec=lookup_ops.StrongHashSpec((1, 2)),
    name="table2")

self.evaluate(lookup_ops.tables_initializer())

input_string = constant_op.constant(
    ["fruit", "brain", "salad", "surgery", "UNK"])

out1 = table1.lookup(input_string)
out2 = table2.lookup(input_string)

out1, out2 = self.evaluate([out1, out2])
self.assertAllEqual([5, 0, 1, 2, 5], out1)
self.assertAllEqual([5, 0, 1, 2, 3], out2)
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table1.size()))
self.assertEqual(vocab_size + oov_buckets, self.evaluate(table2.size()))
if not context.executing_eagerly():
    test_util.assert_ops_in_graph({
        "table1_Lookup/hash_bucket": "StringToHashBucketFast",
        "table2_Lookup/hash_bucket": "StringToHashBucketStrong",
    }, ops.get_default_graph())
