# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
"""Tests object detection model through MLIR converter."""
self._initObjectDetectionArgs()
custom_opdefs_str = (
    'name: \'TFLite_Detection_PostProcess\' '
    'input_arg: { name: \'raw_outputs/box_encodings\' type: DT_FLOAT } '
    'input_arg: { name: \'raw_outputs/class_predictions\' type: DT_FLOAT } '
    'input_arg: { name: \'anchors\' type: DT_FLOAT } '
    'output_arg: { name: \'TFLite_Detection_PostProcess\' type: DT_FLOAT } '
    'output_arg: { name: \'TFLite_Detection_PostProcess:1\' '
    'type: DT_FLOAT } '
    'output_arg: { name: \'TFLite_Detection_PostProcess:2\' '
    'type: DT_FLOAT } '
    'output_arg: { name: \'TFLite_Detection_PostProcess:3\' '
    'type: DT_FLOAT } '
    'attr : { name: \'h_scale\' type: \'float\'} '
    'attr : { name: \'max_classes_per_detection\' type: \'int\'} '
    'attr : { name: \'max_detections\' type: \'int\'} '
    'attr : { name: \'nms_iou_threshold\' type: \'float\'} '
    'attr : { name: \'nms_score_threshold\' type: \'float\'} '
    'attr : { name: \'num_classes\' type: \'int\'} '
    'attr : { name: \'w_scale\' type: \'float\'} '
    'attr : { name: \'x_scale\' type: \'float\'} '
    'attr : { name: \'y_scale\' type: \'float\'}')

flags_str = ('--graph_def_file={0} --input_arrays={1} '
             '--output_arrays={2} --input_shapes={3} '
             '--custom_opdefs="{4}"'.format(self._graph_def_file,
                                            self._input_arrays,
                                            self._output_arrays,
                                            self._input_shapes,
                                            custom_opdefs_str))

# Ensure --allow_custom_ops.
flags_str_final = ('{} --allow_custom_ops').format(flags_str)

self._run(
    flags_str_final,
    should_succeed=True,
    expected_ops_in_converted_model=['TFLite_Detection_PostProcess'])
