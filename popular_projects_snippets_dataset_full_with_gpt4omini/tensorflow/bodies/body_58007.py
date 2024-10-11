# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_phase.py
# Always overwrites the component information, but only overwrites the
# subcomponent if it is not available.
error_data.component = component.value
if not error_data.subcomponent:
    error_data.subcomponent = subcomponent.name
tflite_metrics = metrics.TFLiteConverterMetrics()
tflite_metrics.set_converter_error(error_data)
