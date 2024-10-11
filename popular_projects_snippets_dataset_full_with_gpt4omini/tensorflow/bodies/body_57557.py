# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Constructor for TFLiteConverter.

    Args:
      experimental_debug_info_func: An experimental function to retrieve the
        graph debug info for a set of nodes from the `graph_def`.
    """
super(TFLiteConverterBaseV1, self).__init__()
self.inference_type = _dtypes.float32
self.inference_input_type = None
self.inference_output_type = None
self.output_format = constants.TFLITE
self.quantized_input_stats = {}
self.default_ranges_stats = None
self.drop_control_dependency = True
self.reorder_across_fake_quant = False
self.change_concat_input_ranges = False
self.dump_graphviz_dir = None
self.dump_graphviz_video = False
self.conversion_summary_dir = None
self._debug_info_func = experimental_debug_info_func
self._metadata.environment.apiVersion = 1
