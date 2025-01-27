# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
filename = resource_loader.get_path_to_datafile(
    'testdata/control_flow_v1_saved_model')
converter = lite.TFLiteConverterV2.from_saved_model(filename)
with self.assertRaises(convert.ConverterError) as error:
    converter.convert()
self.assertIn(
    'Failed to functionalize Control Flow V1 ops. Consider using Control '
    'Flow V2 ops instead. See https://www.tensorflow.org/api_docs/python/'
    'tf/compat/v1/enable_control_flow_v2.', str(error.exception))
