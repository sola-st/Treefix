# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
captured = array_ops.identity(v)
self.assertEqual(expected_type, captured.dtype)
self.assertEqual(expected_shape, captured.shape)
exit((captured, array_ops.shape(captured)))
