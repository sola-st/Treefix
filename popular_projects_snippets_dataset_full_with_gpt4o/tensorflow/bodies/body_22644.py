# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils_test.py
self.assertEqual((2, 2, 2), utils.normalize_tuple(2, n=3, name='strides'))
self.assertEqual(
    (2, 1, 2), utils.normalize_tuple((2, 1, 2), n=3, name='strides'))

with self.assertRaises(ValueError):
    utils.normalize_tuple((2, 1), n=3, name='strides')

with self.assertRaises(ValueError):
    utils.normalize_tuple(None, n=3, name='strides')
