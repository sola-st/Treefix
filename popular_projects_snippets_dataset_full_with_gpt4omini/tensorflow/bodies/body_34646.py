# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
default_val = -1
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2, 3, 4], dtypes.int64)

raised_error = ValueError
if context.executing_eagerly():
    raised_error = errors_impl.InvalidArgumentError
with self.assertRaises(raised_error):
    self.getHashTable()(
        lookup_ops.KeyValueTensorInitializer(keys, values),
        default_val,
        experimental_is_anonymous=is_anonymous)
