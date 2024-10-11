# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable(1.0)
    v.assign_add(2.0)
self.assertEqual(3.0, v.numpy())
