# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
self.assertTrue(x is not None and y is not None or x is None and y is None)
self.assertEqual(x.as_list(), y.as_list())
