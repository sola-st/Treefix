# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
self.assertIn(math_ops.abs, dispatch.unary_elementwise_apis())
self.assertIn(math_ops.cos, dispatch.unary_elementwise_apis())
self.assertIn(math_ops.add, dispatch.binary_elementwise_apis())
self.assertIn(math_ops.multiply, dispatch.binary_elementwise_apis())
