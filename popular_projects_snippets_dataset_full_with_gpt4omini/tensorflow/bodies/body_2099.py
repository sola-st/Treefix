# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
self.assertLen(output, 3)
self.assertEqual(output[0].shape.as_list(), list(expected_shape))
self.assertEqual(output[1].shape.as_list(), list(expected_shape))
self.assertEqual(output[2].shape.as_list(), list(expected_shape))
