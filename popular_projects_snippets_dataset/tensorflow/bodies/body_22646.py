# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils_test.py
self.assertEqual('same', utils.normalize_padding('SAME'))
self.assertEqual('valid', utils.normalize_padding('VALID'))

with self.assertRaises(ValueError):
    utils.normalize_padding('invalid')
