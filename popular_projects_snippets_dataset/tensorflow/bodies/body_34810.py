# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
default_val = [-1, -1]
table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)

input_string = constant_op.constant([["brain", "salad"], ["tank",
                                                          "tarkus"]])

invalid_default_val = constant_op.constant(
    [[-2, -3], [-4, -5], [-6, -7], [-8, -9]], dtypes.int64)

with self.assertRaisesRegex(
    (ValueError, errors_impl.InvalidArgumentError),
    "Expected shape \[2\] or \[2,2,2\] for default value, got \[4,2]"):
    self.evaluate(table.lookup(input_string, invalid_default_val))

invalid_default_val = constant_op.constant([[[-2, -3], [-4, -5]]],
                                           dtypes.int64)
with self.assertRaisesRegex(
    (ValueError, errors_impl.InvalidArgumentError),
    "Expected shape \[2\] or \[2,2,2\] for default value, got \[1,2,2\]"):
    self.evaluate(table.lookup(input_string, invalid_default_val))
