# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
scalar = "hello"
scalar_expanded = array_ops.expand_dims(scalar, [0])
self.assertEqual(scalar_expanded.get_shape(), (1,))
