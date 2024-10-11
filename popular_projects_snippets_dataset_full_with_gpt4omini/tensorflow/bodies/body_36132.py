# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([0, 1, 2, 3])
copy_to_graph = ops.Graph()
with copy_to_graph.as_default():  # Intentionally testing v1 behavior
    copied = resource_variable_ops.copy_to_graph_uninitialized(v)
    self.assertEqual(v.name, copied.name)
    self.assertIsNone(copied.initializer)
