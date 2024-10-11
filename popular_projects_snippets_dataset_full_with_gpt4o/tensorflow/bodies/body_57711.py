# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
graph_def_file = resource_loader.get_path_to_datafile(
    'testdata/control_flow_v1.pbtxt')
input_arrays = ['a', 'b', 'c', 'd']
output_arrays = ['Merge']

converter = lite.TFLiteConverter.from_frozen_graph(graph_def_file,
                                                   input_arrays,
                                                   output_arrays)
with self.assertRaises(ConverterError) as error:
    converter.convert()
self.assertIn(
    'Failed to functionalize Control Flow V1 ops. Consider using Control '
    'Flow V2 ops instead. See https://www.tensorflow.org/api_docs/python/'
    'tf/compat/v1/enable_control_flow_v2.', str(error.exception))
