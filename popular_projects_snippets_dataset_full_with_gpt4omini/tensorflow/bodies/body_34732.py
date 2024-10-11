# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = lookup_ops.DenseHashTable(
    dtypes.int64,
    dtypes.int64,
    default_value=-1,
    empty_key=0,
    deleted_key=-1,
    experimental_is_anonymous=is_anonymous)

# Inserting the empty key returns an error
keys1 = constant_op.constant([11, 0], dtypes.int64)
values1 = constant_op.constant([0, 1], dtypes.int64)
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "empty_key"):
    self.evaluate(table.insert(keys1, values1))

# Looking up the empty key returns an error
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "empty_key"):
    self.evaluate(table.lookup(keys1))

# Inserting the deleted key returns an error
keys2 = constant_op.constant([11, -1], dtypes.int64)
values2 = constant_op.constant([0, 1], dtypes.int64)
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "deleted_key"):
    self.evaluate(table.insert(keys2, values2))

# Looking up the empty key returns an error
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "deleted_key"):
    self.evaluate(table.lookup(keys2))

# Arbitrary tensors of keys are not supported
keys = constant_op.constant([[11, 0], [12, 1]], dtypes.int64)
values = constant_op.constant([[11, 0], [12, 1]], dtypes.int64)
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Expected key shape"):
    self.evaluate(table.lookup(keys))
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Expected key shape"):
    self.evaluate(table.insert(keys, values))

with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Number of buckets must be"):
    table2 = lookup_ops.DenseHashTable(
        dtypes.int64,
        dtypes.int64,
        default_value=-1,
        empty_key=17,
        deleted_key=-1,
        initial_num_buckets=12,
        experimental_is_anonymous=is_anonymous)
    self.assertAllEqual(0, self.evaluate(table2.size()))

with self.assertRaisesRegex(
    errors_impl.InvalidArgumentError,
    "Empty and deleted keys must have same shape"):
    table3 = lookup_ops.DenseHashTable(
        dtypes.int64,
        dtypes.int64,
        default_value=-1,
        empty_key=42,
        deleted_key=[1, 2],
        experimental_is_anonymous=is_anonymous)
    self.assertAllEqual(0, self.evaluate(table3.size()))

with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Empty and deleted keys cannot be equal"):
    table4 = lookup_ops.DenseHashTable(
        dtypes.int64,
        dtypes.int64,
        default_value=-1,
        empty_key=42,
        deleted_key=42,
        experimental_is_anonymous=is_anonymous)
    self.assertAllEqual(0, self.evaluate(table4.size()))

with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Empty and deleted keys cannot be equal"):
    table5 = lookup_ops.DenseHashTable(
        dtypes.int64,
        dtypes.int64,
        default_value=-1,
        empty_key=[1, 2, 3],
        deleted_key=[1, 2, 3],
        experimental_is_anonymous=is_anonymous)
    self.assertAllEqual(0, self.evaluate(table5.size()))
