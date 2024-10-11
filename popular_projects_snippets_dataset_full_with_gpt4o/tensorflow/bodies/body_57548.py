# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        No concrete functions is specified.
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """
if self.experimental_lower_to_saved_model:
    saved_model_convert_result = self._convert_as_saved_model()
    if saved_model_convert_result:
        exit(saved_model_convert_result)

graph_def, input_tensors, output_tensors, frozen_func = (
    self._freeze_concrete_function())

graph_def = self._optimize_tf_model(graph_def, input_tensors,
                                    output_tensors, frozen_func)

exit(super(TFLiteFrozenGraphConverterV2,
             self).convert(graph_def, input_tensors, output_tensors))
