# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
constraint = lambda x: x
v = resource_variable_ops.ResourceVariable(
    initial_value=lambda: 1, constraint=constraint, name="var0")
self.assertEqual(v.constraint, constraint)

constraint = 0
with self.assertRaises(ValueError):
    v = resource_variable_ops.ResourceVariable(
        initial_value=lambda: 1, constraint=constraint, name="var1")
