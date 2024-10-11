# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = os.path.join(self.get_temp_dir(), "three_columns.txt")
with open(vocabulary_file, "w") as f:
    f.write("\n".join(["0\tbrain\t1", "1\tsalad\t5", "2\tsurgery\t6"]) + "\n")

with self.cached_session():
    default_value = -1
    key_index = 2
    value_index = 1
    init = lookup_ops.TextFileInitializer(
        vocabulary_file, dtypes.string, key_index, dtypes.int64, value_index)
    self.assertIn("three_columns.txt_2_1", init._shared_name)
    with self.assertRaisesOpError("is not a valid"):
        table = self.getHashTable()(
            init, default_value, experimental_is_anonymous=is_anonymous)
        self.initialize_table(table)
