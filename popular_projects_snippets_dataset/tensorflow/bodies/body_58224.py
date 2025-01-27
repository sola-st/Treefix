# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
filename = resource_loader.get_path_to_datafile(
    '../testdata/control_flow_v1_saved_model')
converter = lite.TFLiteConverterV2.from_saved_model(filename)
self.convert_and_check_location_info(
    converter, converter_error_data_pb2.ConverterErrorData.UNKNOWNLOC)
exported_error = metrics._gauge_conversion_errors.get_cell(
    'CONVERT_TF_TO_TFLITE_MODEL', 'CONVERT_SAVED_MODEL', '',
    'ERROR_UNSUPPORTED_CONTROL_FLOW_V1').value()
self.assertEqual(
    exported_error,
    'Merge only has 4 inputs, while only merge nodes with two inputs '
    'supported.\n\tFailed to functionalize Control Flow V1 ops. Consider '
    'using Control Flow V2 ops instead. See https://www.tensorflow.org/'
    'api_docs/python/tf/compat/v1/enable_control_flow_v2.')
