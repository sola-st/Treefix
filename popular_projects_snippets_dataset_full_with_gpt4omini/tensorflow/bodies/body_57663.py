# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with self.assertRaises(IOError) as error:
    lite.TFLiteConverter.from_frozen_graph('invalid_file', ['Placeholder'],
                                           ['add'])
self.assertEqual('File \'invalid_file\' does not exist.',
                 str(error.exception))
