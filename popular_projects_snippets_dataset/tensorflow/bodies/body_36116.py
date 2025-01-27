# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    # Scalars use a separate code path.
    v1 = resource_variable_ops.ResourceVariable(initial_value=lambda: 1,
                                                name="v1")
    self.assertEqual(1, np.array(v1))

    v2 = resource_variable_ops.ResourceVariable(initial_value=lambda: [1, 2],
                                                name="v2")
    self.assertAllEqual(v2.read_value().numpy(), np.array(v2))
    self.assertAllEqual([1, 2], np.array(v2))
