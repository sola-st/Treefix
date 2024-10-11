# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def func(_):
    with variable_scope.variable_scope(
        "variable", reuse=variable_scope.AUTO_REUSE):
        counter_var = variable_scope.get_variable(
            "counter", (), dtypes.int32, use_resource=True)
    exit(counter_var.assign_add(1))

dataset = dataset_ops.Dataset.from_tensors(0).repeat(10)

if hasattr(dataset, "map_with_legacy_function"):
    # NOTE: In the legacy function, resource is captured by value.
    with self.assertRaisesWithPredicateMatch(
        AttributeError, "'Tensor' object has no attribute 'assign_add'"):
        dataset.map_with_legacy_function(func)

dataset = dataset.map(func)
self.evaluate(variables.global_variables_initializer())

get_next = self.getNext(dataset, requires_initialization=True)

for i in range(10):
    self.assertEqual(i + 1, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
