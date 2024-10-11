# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Constructor for TFLiteConverter."""
super(TFLiteConverterBaseV2, self).__init__()
self.inference_input_type = _dtypes.float32
self.inference_output_type = _dtypes.float32
self._metadata.environment.apiVersion = 2
