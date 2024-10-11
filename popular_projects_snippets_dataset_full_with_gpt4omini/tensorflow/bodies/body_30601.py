# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with ops.Graph().as_default():
    var = variables.Variable([[1.0, 1.0]])
self.assertDeviceEqual(None, var.device)
self.assertDeviceEqual(None, var.initializer.device)
