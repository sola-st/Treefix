# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("f2i_vocab1.txt")
vocabulary_file = constant_op.constant(vocabulary_file)
table = lookup_ops.index_table_from_file(
    vocabulary_file=vocabulary_file, num_oov_buckets=1)
ids = table.lookup(constant_op.constant(["salad", "surgery", "tarkus"]))

if not context.executing_eagerly():
    with self.assertRaises(errors_impl.OpError):
        self.evaluate(ids)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((1, 2, 3), self.evaluate(ids))
if not context.executing_eagerly():
    self.assertEqual(1,
                     len(ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS)))
