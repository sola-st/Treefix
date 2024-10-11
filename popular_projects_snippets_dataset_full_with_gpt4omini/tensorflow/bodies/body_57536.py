# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a TensorFlow GraphDef based on instance variables.

    Args:
      graph_def: Frozen TensorFlow GraphDef.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        No concrete functions is specified.
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """
self._validate_inputs(graph_def, input_tensors)
converter_kwargs = self._get_base_converter_args()
converter_kwargs.update(self._quant_mode.converter_flags())
if not self.experimental_new_converter:
    logging.warning(
        "Please consider switching to the new converter by setting "
        "experimental_new_converter=True. "
        "The old converter is deprecated.")
else:
    logging.info("Using new converter: If you encounter a problem "
                 "please file a bug. You can opt-out "
                 "by setting experimental_new_converter=False")

# Converts model.
result = _convert_graphdef(
    input_data=graph_def,
    input_tensors=input_tensors,
    output_tensors=output_tensors,
    **converter_kwargs)

exit(self._optimize_tflite_model(
    result, self._quant_mode, quant_io=self.experimental_new_quantizer))
