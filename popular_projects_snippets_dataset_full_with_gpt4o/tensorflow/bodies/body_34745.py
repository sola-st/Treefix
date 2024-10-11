# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("f2i_vocab5.txt")
table = lookup_ops.index_table_from_file(
    vocabulary_file=vocabulary_file, num_oov_buckets=1000)
ids = table.lookup(
    constant_op.constant(["salad", "surgery", "tarkus", "toccata"]))

if not context.executing_eagerly():
    with self.assertRaises(errors_impl.OpError):
        self.evaluate(ids)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual(
    (
        1,  # From vocabulary file.
        2,  # From vocabulary file.
        867,  # 3 + fingerprint("tarkus") mod 300.
        860),  # 3 + fingerprint("toccata") mod 300.
    self.evaluate(ids))
