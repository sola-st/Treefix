# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    v1 = resource_variable_ops.ResourceVariable(initial_value=lambda: 1,
                                                name="same")
    with ops.container("different"):
        v2 = resource_variable_ops.ResourceVariable(initial_value=lambda: 0,
                                                    name="same")
    v2.assign(2)
    self.assertEqual(1, v1.read_value().numpy())
    self.assertEqual(2, v2.read_value().numpy())
