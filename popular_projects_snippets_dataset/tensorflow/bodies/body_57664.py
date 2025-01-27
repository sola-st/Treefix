# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
graph_def_file = os.path.join(self.get_temp_dir(), 'invalid_file')
with gfile.Open(graph_def_file, 'wb') as temp_file:
    temp_file.write('bad data')
    temp_file.flush()

# Attempts to convert the invalid model.
with self.assertRaises(IOError) as error:
    lite.TFLiteConverter.from_frozen_graph(graph_def_file, ['Placeholder'],
                                           ['add'])
self.assertEqual(
    'Unable to parse input file \'{}\'.'.format(graph_def_file),
    str(error.exception))
