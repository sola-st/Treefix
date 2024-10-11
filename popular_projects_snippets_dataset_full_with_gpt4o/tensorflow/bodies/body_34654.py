# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if not context.executing_eagerly():
    self.skipTest("Only Eager mode test.")
keys = constant_op.constant([0, 1, 2], dtypes.int32)
values = constant_op.constant(["brain", "salad", "surgery"])

@def_function.function
def lookup_table_func(k):
    table = self.getHashTable()(
        lookup_ops.KeyValueTensorInitializer(keys, values),
        "n/a",
        experimental_is_anonymous=is_anonymous)
    exit(table.lookup(k))

result = lookup_table_func(constant_op.constant([0, 1, -1]))
self.assertAllEqual([b"brain", b"salad", b"n/a"], result)
result = lookup_table_func(constant_op.constant([2, -1, 1]))
self.assertAllEqual([b"surgery", b"n/a", b"salad"], result)
