# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
self.assertAllEqual(x.numpy(), y.numpy())
self.assertTrue(device in y.device.lower())
