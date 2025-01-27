# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocab_file = self._createVocabFile("feat_to_id_4.txt")
default_value = -1
vocab_size = 3
oov_buckets = 1
lookup_table = lookup_ops.StaticHashTable(
    lookup_ops.TextFileIdTableInitializer(
        vocab_file, vocab_size=vocab_size), default_value)

with self.assertRaises(TypeError):
    lookup_ops.IdTableWithHashBuckets(
        lookup_table, oov_buckets, hasher_spec=1)

table = lookup_ops.IdTableWithHashBuckets(
    lookup_table,
    oov_buckets,
    hasher_spec=lookup_ops.HasherSpec("my-awesome-hash", None))

input_string = constant_op.constant(["brain", "salad", "surgery", "UNK"])

with self.assertRaises(ValueError):
    table.lookup(input_string)

with self.assertRaises(ValueError):
    table = lookup_ops.IdTableWithHashBuckets(
        lookup_table, oov_buckets, hasher_spec=lookup_ops.StrongHashSpec([]))

with self.assertRaises(ValueError):
    table = lookup_ops.IdTableWithHashBuckets(
        lookup_table,
        oov_buckets,
        hasher_spec=lookup_ops.StrongHashSpec([1, 2, 3]))

with self.assertRaises(TypeError):
    table = lookup_ops.IdTableWithHashBuckets(
        lookup_table,
        oov_buckets,
        hasher_spec=lookup_ops.StrongHashSpec([None, 2]))
