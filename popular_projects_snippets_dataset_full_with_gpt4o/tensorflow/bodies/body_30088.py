# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
scalar = "hello"
scalar_squeezed = array_ops.squeeze(scalar, ())
self.assertEqual(scalar_squeezed.get_shape(), ())
