# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_list = constant_op.constant(["hello", "hello"])
table = lookup_ops.index_to_string_table_from_tensor(
    vocabulary_list=vocabulary_list)
indices = constant_op.constant([0, 1, 4], dtypes.int64)
features = table.lookup(indices)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((b"hello", b"hello", b"UNK"), self.evaluate(features))
