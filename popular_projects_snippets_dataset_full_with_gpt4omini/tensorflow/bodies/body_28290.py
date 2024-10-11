# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
counter_var = variable_scope.get_variable(
    "counter", (), dtypes.int32, use_resource=True)
dataset = dataset_ops.Dataset.from_tensors(0).repeat(10)
dataset = apply_map(dataset, lambda _: counter_var.assign_add(1))
options = options_lib.Options()
options.experimental_optimization.inject_prefetch = False
dataset = dataset.with_options(options)
get_next = self.getNext(dataset, requires_initialization=True)

self.evaluate(counter_var.initializer)

for i in range(10):
    self.assertEqual(i, self.evaluate(counter_var))
    self.assertEqual(i + 1, self.evaluate(get_next()))
self.assertEqual(10, self.evaluate(counter_var))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
self.assertEqual(10, self.evaluate(counter_var))
