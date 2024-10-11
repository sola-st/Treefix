# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
with context.graph_mode():
    inner = data_structures.List()
    outer = data_structures.List([inner])
    inner.append(non_keras_core.Dense(1))
    inner[0](array_ops.ones([2, 3]))
    self.assertEqual(2, len(outer.variables))
    self.assertIsInstance(
        outer.variables[0],
        resource_variable_ops.ResourceVariable)
