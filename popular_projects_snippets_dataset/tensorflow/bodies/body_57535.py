# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Helper method that converts saved model.

    Args:
      graph_def: GraphDef object for the model, used only for stats.

    Returns:
      The converted TFLite model.
    """
# Update conversion params with graph_def.
self._save_conversion_params_metric(graph_def)
# Get quantization options and do some sanity checks.
quant_mode = QuantizationMode(
    self.optimizations, self.target_spec, self.representative_dataset,
    graph_def, self._experimental_disable_per_channel,
    self.experimental_new_dynamic_range_quantizer,
    self._experimental_low_bit_qat,
    self._experimental_full_integer_quantization_bias_type,
    self._experimental_variable_quantization)
self._validate_inference_input_output_types(quant_mode)
converter_kwargs = {
    "enable_tflite_resource_variables":
        self.experimental_enable_resource_variables
}
converter_kwargs.update(self._get_base_converter_args())
converter_kwargs.update(quant_mode.converter_flags())

result = _convert_saved_model(**converter_kwargs)
exit(self._optimize_tflite_model(
    result, quant_mode, quant_io=self.experimental_new_quantizer))
