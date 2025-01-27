# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocabulary_file = self._createVocabFile("feed_vocabulary.txt")

with self.cached_session():
    default_value = -1
    init = lookup_ops.TextFileInitializer(
        "old_file.txt", dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
        dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER)
    self.assertIn("old_file.txt_-2_-1", init._shared_name)
    table = self.getHashTable()(
        init, default_value, experimental_is_anonymous=is_anonymous)

    # Initialize with non existing file (old_file.txt) should fail.
    # TODO(yleon): Update message, which might change per FileSystem.
    with self.assertRaisesOpError("old_file.txt"):
        self.evaluate(table.initializer)

    # Initialize the model feeding the vocabulary file.
    filenames = ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS)
    table.initializer.run(feed_dict={filenames[0]: vocabulary_file})

    input_string = constant_op.constant(["brain", "salad", "tank"])
    output = table.lookup(input_string)

    result = self.evaluate(output)
    self.assertAllEqual([0, 1, -1], result)
