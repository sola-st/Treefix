# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
with self.cached_session():
    default_value = -1
    with self.assertRaises(ValueError):
        self.getHashTable()(
            lookup_ops.TextFileInitializer(
                "", dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
                dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER),
            default_value,
            experimental_is_anonymous=is_anonymous)
