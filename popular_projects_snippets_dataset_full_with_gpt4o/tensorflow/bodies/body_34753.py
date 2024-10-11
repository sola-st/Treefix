# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("invalid_hasher.txt")
with self.assertRaises(TypeError):
    lookup_ops.index_table_from_file(
        vocabulary_file=vocabulary_file,
        vocab_size=3,
        num_oov_buckets=1,
        hasher_spec=1)

table = lookup_ops.index_table_from_file(
    vocabulary_file=vocabulary_file,
    vocab_size=3,
    num_oov_buckets=1,
    hasher_spec=lookup_ops.HasherSpec("my-awesome-hash", None))

self.assertRaises(ValueError, table.lookup,
                  constant_op.constant(["salad", "surgery", "tarkus"]))
