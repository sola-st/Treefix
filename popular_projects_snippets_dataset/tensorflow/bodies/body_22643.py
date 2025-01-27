# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils_test.py
self.assertEqual('NCDHW', utils.convert_data_format('channels_first', 5))
self.assertEqual('NCHW', utils.convert_data_format('channels_first', 4))
self.assertEqual('NCW', utils.convert_data_format('channels_first', 3))
self.assertEqual('NHWC', utils.convert_data_format('channels_last', 4))
self.assertEqual('NWC', utils.convert_data_format('channels_last', 3))
self.assertEqual('NDHWC', utils.convert_data_format('channels_last', 5))

with self.assertRaises(ValueError):
    utils.convert_data_format('invalid', 2)
