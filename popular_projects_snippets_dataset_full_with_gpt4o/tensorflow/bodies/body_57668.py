# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
# Initializes the arguments required for the object detection model.
# Looks for the model file which is saved in a different location internally
# and externally.
filename = resource_loader.get_path_to_datafile('testdata/tflite_graph.pb')
if not os.path.exists(filename):
    filename = os.path.join(
        resource_loader.get_root_dir_with_all_resources(),
        '../tflite_mobilenet_ssd_quant_protobuf/tflite_graph.pb')
    if not os.path.exists(filename):
        raise IOError("File '{0}' does not exist.".format(filename))

self._graph_def_file = filename
self._input_arrays = ['normalized_input_image_tensor']
self._output_arrays = [
    'TFLite_Detection_PostProcess', 'TFLite_Detection_PostProcess:1',
    'TFLite_Detection_PostProcess:2', 'TFLite_Detection_PostProcess:3'
]
self._input_shapes = {'normalized_input_image_tensor': [1, 300, 300, 3]}
