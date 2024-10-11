# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v = resource_variable_ops.ResourceVariable(True)
    i = array_ops.identity(v)
self.assertAllEqual(True, i.numpy())
