# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocabulary_file = self._createVocabFile("one_column_2.txt")

with self.cached_session():
    default_value = "UNK"
    key_index = lookup_ops.TextFileIndex.LINE_NUMBER
    value_index = lookup_ops.TextFileIndex.WHOLE_LINE
    init = lookup_ops.TextFileInitializer(
        vocabulary_file, dtypes.int64, key_index, dtypes.string, value_index)
    self.assertIn("one_column_2.txt_-1_-2", init._shared_name)
    table = self.getHashTable()(
        init, default_value, experimental_is_anonymous=is_anonymous)
    self.initialize_table(table)

    input_values = constant_op.constant([0, 1, 2, 3], dtypes.int64)
    output = table.lookup(input_values)

    result = self.evaluate(output)
    self.assertAllEqual([b"brain", b"salad", b"surgery", b"UNK"], result)
