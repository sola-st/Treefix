# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = lookup_ops.index_table_from_tensor(
    vocabulary_list=(42, 1, -1000), num_oov_buckets=1, dtype=dtypes.int64)
ids = table.lookup(constant_op.constant((1, -1000, 11), dtype=dtypes.int64))

if not context.executing_eagerly():
    with self.assertRaises(errors_impl.FailedPreconditionError):
        self.evaluate(ids)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((1, 2, 3), self.evaluate(ids))
