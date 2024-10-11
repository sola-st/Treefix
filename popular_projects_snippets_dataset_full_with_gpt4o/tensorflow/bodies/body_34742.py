# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile(
    "f2i_vocab2.txt", values=("42", "1", "-1000"))
table = lookup_ops.index_table_from_file(
    vocabulary_file=vocabulary_file,
    num_oov_buckets=1,
    key_dtype=dtypes.int32)
ids = table.lookup(constant_op.constant((1, -1000, 11), dtype=dtypes.int32))

if not context.executing_eagerly():
    with self.assertRaises(errors_impl.OpError):
        self.evaluate(ids)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((1, 2, 3), self.evaluate(ids))
