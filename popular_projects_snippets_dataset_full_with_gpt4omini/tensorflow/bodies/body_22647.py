# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils_test.py
self.assertEqual(4, utils.conv_output_length(4, 2, 'same', 1, 1))
self.assertEqual(2, utils.conv_output_length(4, 2, 'same', 2, 1))
self.assertEqual(3, utils.conv_output_length(4, 2, 'valid', 1, 1))
self.assertEqual(2, utils.conv_output_length(4, 2, 'valid', 2, 1))
self.assertEqual(5, utils.conv_output_length(4, 2, 'full', 1, 1))
self.assertEqual(3, utils.conv_output_length(4, 2, 'full', 2, 1))
self.assertEqual(2, utils.conv_output_length(5, 2, 'valid', 2, 2))
