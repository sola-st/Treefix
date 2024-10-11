# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with ops.Graph().as_default():
    with ops.device("/job:ps"):
        var = variables.Variable([[1.0, 1.0]])
self.assertDeviceEqual("/job:ps", var.device)
self.assertDeviceEqual("/job:ps", var.initializer.device)
