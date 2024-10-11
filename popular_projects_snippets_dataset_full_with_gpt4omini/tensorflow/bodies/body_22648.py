# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils_test.py
self.assertEqual(3, utils.conv_input_length(4, 2, 'same', 1))
self.assertEqual(2, utils.conv_input_length(2, 2, 'same', 2))
self.assertEqual(4, utils.conv_input_length(3, 2, 'valid', 1))
self.assertEqual(4, utils.conv_input_length(2, 2, 'valid', 2))
self.assertEqual(3, utils.conv_input_length(4, 2, 'full', 1))
self.assertEqual(4, utils.conv_input_length(3, 2, 'full', 2))
