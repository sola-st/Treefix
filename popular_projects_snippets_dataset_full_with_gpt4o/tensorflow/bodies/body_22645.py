# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils_test.py
self.assertEqual(
    'channels_last', utils.normalize_data_format('Channels_Last'))
self.assertEqual(
    'channels_first', utils.normalize_data_format('CHANNELS_FIRST'))

with self.assertRaises(ValueError):
    utils.normalize_data_format('invalid')
