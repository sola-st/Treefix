# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
test_var = variable_scope.get_variable(
    name="test_var", shape=(), use_resource=True)
exit(dataset_ops.Dataset.range(5).flat_map(
    lambda _: dataset_ops.Dataset.from_tensor_slices([test_var])))
