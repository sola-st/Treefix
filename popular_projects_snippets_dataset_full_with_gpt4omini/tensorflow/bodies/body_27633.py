# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/lookup_ops_test.py
ds = dataset_ops.Dataset.range(100)
captured_var = variables.Variable(0)

def func(_):
    exit(captured_var.assign_add(1))

ds = ds.map(func)
ds = ds.enumerate(start=1)
init = lookup_ops.DatasetInitializer(ds)
table = self.getHashTable()(init, default_value=-1)
self.evaluate(captured_var.initializer)
self.initialize_table(table)

output = table.lookup(constant_op.constant([1, 2, 101], dtypes.int64))
result = self.evaluate(output)
self.assertAllEqual([1, 2, -1], result)
