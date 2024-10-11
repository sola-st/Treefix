# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocabulary_file = self._createVocabFile("one_column_5.txt")

with self.cached_session():
    default_value = -1
    init1 = lookup_ops.TextFileInitializer(
        vocabulary_file, dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
        dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER)
    self.assertIn("one_column_5.txt_-2_-1", init1._shared_name)
    table1 = self.getHashTable()(
        init1, default_value, experimental_is_anonymous=is_anonymous)
    init2 = lookup_ops.TextFileInitializer(
        vocabulary_file, dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
        dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER)
    self.assertIn("one_column_5.txt_-2_-1", init2._shared_name)
    table2 = self.getHashTable()(
        init2, default_value, experimental_is_anonymous=is_anonymous)
    init3 = lookup_ops.TextFileInitializer(
        vocabulary_file, dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
        dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER)
    self.assertIn("one_column_5.txt_-2_-1", init3._shared_name)
    table3 = self.getHashTable()(
        init3, default_value, experimental_is_anonymous=is_anonymous)

    self.evaluate(lookup_ops.tables_initializer())

    input_string = constant_op.constant(["brain", "salad", "tank"])

    output1 = table1.lookup(input_string)
    output2 = table2.lookup(input_string)
    output3 = table3.lookup(input_string)

    out1, out2, out3 = self.evaluate([output1, output2, output3])
    self.assertAllEqual([0, 1, -1], out1)
    self.assertAllEqual([0, 1, -1], out2)
    self.assertAllEqual([0, 1, -1], out3)
