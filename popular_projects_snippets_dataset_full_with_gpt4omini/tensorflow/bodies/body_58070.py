# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
self.assertAllEqual(scales, params['scales'])
self.assertAllEqual(zero_points, params['zero_points'])
self.assertEqual(quantized_dimension, params['quantized_dimension'])
