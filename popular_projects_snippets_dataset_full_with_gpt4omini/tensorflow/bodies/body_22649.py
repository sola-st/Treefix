# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils_test.py
self.assertEqual(4, utils.deconv_output_length(4, 2, 'same', 1))
self.assertEqual(8, utils.deconv_output_length(4, 2, 'same', 2))
self.assertEqual(5, utils.deconv_output_length(4, 2, 'valid', 1))
self.assertEqual(8, utils.deconv_output_length(4, 2, 'valid', 2))
self.assertEqual(3, utils.deconv_output_length(4, 2, 'full', 1))
self.assertEqual(6, utils.deconv_output_length(4, 2, 'full', 2))
