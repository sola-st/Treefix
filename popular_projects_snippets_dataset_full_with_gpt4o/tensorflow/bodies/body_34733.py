# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
v = variables.Variable(1.)
v1 = variables.Variable(1.)
table = lookup_ops.DenseHashTable(
    dtypes.string,
    dtypes.resource,
    default_value=v.handle,
    empty_key="<empty>",
    deleted_key="<deleted>",
    experimental_is_anonymous=is_anonymous)
self.assertEqual([], table.lookup("not_found").shape)
table.insert("v1", v1.handle)
self.assertEqual([], table.lookup("v1").shape)
