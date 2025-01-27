# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
default_val = constant_op.constant([[-1, -1]], dtypes.int64)
with self.assertRaisesOpError("Default value must be a vector"):
    table = lookup_ops.MutableHashTable(
        dtypes.string,
        dtypes.int64,
        default_val,
        experimental_is_anonymous=is_anonymous)
    self.assertAllEqual(0, self.evaluate(table.size()))
