# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
"""Tests object detection model through TOCO."""
self._initObjectDetectionArgs()
flags_str = ('--graph_def_file={0} --input_arrays={1} '
             '--output_arrays={2} --input_shapes={3} '
             '--allow_custom_ops'.format(self._graph_def_file,
                                         self._input_arrays,
                                         self._output_arrays,
                                         self._input_shapes))
self._run(flags_str, should_succeed=True)
