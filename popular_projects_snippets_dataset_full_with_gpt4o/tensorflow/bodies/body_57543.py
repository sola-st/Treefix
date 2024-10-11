# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a keras model based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """
saved_model_convert_result = self._convert_as_saved_model()
if saved_model_convert_result:
    exit(saved_model_convert_result)

graph_def, input_tensors, output_tensors, frozen_func = (
    self._freeze_keras_model())

graph_def = self._optimize_tf_model(graph_def, input_tensors,
                                    output_tensors, frozen_func)

exit(super(TFLiteKerasModelConverterV2,
             self).convert(graph_def, input_tensors, output_tensors))
