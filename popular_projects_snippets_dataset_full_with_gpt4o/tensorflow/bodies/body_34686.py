# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("filename_shape.txt")

with self.cached_session():
    default_value = -1

    # Invalid data type
    other_type = constant_op.constant(1)
    with self.assertRaises(Exception) as cm:
        self.getHashTable()(
            lookup_ops.TextFileInitializer(
                other_type, dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
                dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER),
            default_value,
            experimental_is_anonymous=is_anonymous)
    self.assertIsInstance(cm.exception, (ValueError, TypeError))

    # Non-scalar filename
    filenames = constant_op.constant([vocabulary_file, vocabulary_file])
    if not context.executing_eagerly():
        with self.assertRaises(Exception) as cm:
            self.getHashTable()(
                lookup_ops.TextFileInitializer(
                    filenames, dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
                    dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER),
                default_value,
                experimental_is_anonymous=is_anonymous)
        self.assertIsInstance(cm.exception, (ValueError, TypeError))
    else:
        with self.assertRaises(errors_impl.InvalidArgumentError):
            self.getHashTable()(
                lookup_ops.TextFileInitializer(
                    filenames, dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
                    dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER),
                default_value,
                experimental_is_anonymous=is_anonymous)
