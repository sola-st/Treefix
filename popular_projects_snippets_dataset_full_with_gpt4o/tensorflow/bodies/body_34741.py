# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("f2i_vocab1.txt")
with self.cached_session():
    vocabulary_placeholder = array_ops.placeholder(dtypes.string, [])
    table = lookup_ops.index_table_from_file(
        vocabulary_file=vocabulary_placeholder, num_oov_buckets=1)
    ids = table.lookup(constant_op.constant(["salad", "surgery", "tarkus"]))

    with self.assertRaises(errors_impl.OpError):
        self.evaluate(ids)

    feed_dict = {vocabulary_placeholder.name: vocabulary_file}
    lookup_ops.tables_initializer().run(feed_dict=feed_dict)
    self.assertAllEqual((1, 2, 3), self.evaluate(ids))
    self.assertEqual(0,
                     len(ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS)))
