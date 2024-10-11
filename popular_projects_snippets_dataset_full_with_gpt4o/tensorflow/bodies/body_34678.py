# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocabulary_file = os.path.join(self.get_temp_dir(), "three_columns.txt")
with open(vocabulary_file, "w") as f:
    f.write("\n".join(["0\tbrain\t1", "1\tsalad\t5", "2\tsurgery\t6"]) + "\n")

with self.cached_session():
    default_value = -1
    key_index = 1
    value_index = 2

    init = lookup_ops.TextFileInitializer(
        vocabulary_file, dtypes.string, key_index, dtypes.int64, value_index)
    self.assertIn("three_columns.txt_1_2", init._shared_name)
    table = self.getHashTable()(
        init, default_value, experimental_is_anonymous=is_anonymous)
    self.initialize_table(table)

    input_string = constant_op.constant(["brain", "salad", "surgery"])
    output = table.lookup(input_string)

    result = self.evaluate(output)
    self.assertAllEqual([1, 5, 6], result)
