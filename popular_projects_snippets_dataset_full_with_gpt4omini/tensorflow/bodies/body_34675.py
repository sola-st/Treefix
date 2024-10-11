# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocabulary_file = self._createVocabFile("one_column_1.txt")
default_value = -1
init = lookup_ops.TextFileInitializer(
    vocabulary_file, dtypes.string, lookup_ops.TextFileIndex.WHOLE_LINE,
    dtypes.int64, lookup_ops.TextFileIndex.LINE_NUMBER)
self.assertIn("one_column_1.txt_-2_-1", init._shared_name)
table = self.getHashTable()(
    init, default_value, experimental_is_anonymous=is_anonymous)
self.initialize_table(table)

output = table.lookup(constant_op.constant(["brain", "salad", "tank"]))

result = self.evaluate(output)
self.assertAllEqual([0, 1, -1], result)
