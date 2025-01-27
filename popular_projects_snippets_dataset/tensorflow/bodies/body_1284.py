# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable(1.0)
    val1 = v.read_value()
    v.assign_add(2.0)
    val2 = v.read_value()
self.assertEqual(1.0, val1.numpy())
self.assertEqual(3.0, val2.numpy())
