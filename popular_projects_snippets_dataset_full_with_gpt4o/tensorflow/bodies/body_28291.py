# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
counter_var = variable_scope.get_variable(
    "counter", (), dtypes.int32, use_resource=True)
dataset = dataset_ops.Dataset.from_tensors(0).repeat(10)
dataset = apply_map(dataset, lambda _: counter_var.assign_add(1))

get_next = self.getNext(dataset, requires_initialization=True)
with self.assertRaises(errors.NotFoundError):
    self.evaluate(get_next())
