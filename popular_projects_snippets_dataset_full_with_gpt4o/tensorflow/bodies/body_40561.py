# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
with context.device('/gpu:0'):
    v = resource_variable_ops.ResourceVariable(True)
self.assertAllEqual(True, array_ops.identity(v))
