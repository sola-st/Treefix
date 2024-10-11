# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
"""Tests object detection model through MLIR converter."""
self._initObjectDetectionArgs()

flags_str = ('--graph_def_file={0} --input_arrays={1} '
             '--output_arrays={2} --input_shapes={3}'.format(
                 self._graph_def_file, self._input_arrays,
                 self._output_arrays, self._input_shapes))

# Valid conversion.
flags_str_final = (
    '{} --allow_custom_ops '
    '--experimental_new_converter '
    '--experimental_select_user_tf_ops=TFLite_Detection_PostProcess '
    '--target_ops=TFLITE_BUILTINS,SELECT_TF_OPS').format(flags_str)
self._run(
    flags_str_final,
    should_succeed=True,
    expected_ops_in_converted_model=['FlexTFLite_Detection_PostProcess'])
