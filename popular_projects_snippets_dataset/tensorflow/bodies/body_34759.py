# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
default_value = -42
table = lookup_ops.index_table_from_tensor(
    vocabulary_list=["brain", "salad", "surgery"],
    default_value=default_value)
ids = table.lookup(constant_op.constant(["salad", "surgery", "tarkus"]))

if not context.executing_eagerly():
    with self.assertRaises(errors_impl.FailedPreconditionError):
        self.evaluate(ids)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((1, 2, default_value), self.evaluate(ids))
