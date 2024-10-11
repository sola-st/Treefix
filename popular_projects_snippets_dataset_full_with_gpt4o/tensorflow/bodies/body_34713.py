# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Empty and deleted keys"):
    table = lookup_ops.DenseHashTable(
        dtypes.int64,
        dtypes.int64,
        default_value=-1,
        empty_key=42,
        deleted_key=42,
        experimental_is_anonymous=is_anonymous)
    self.assertAllEqual(0, self.evaluate(table.size()))
