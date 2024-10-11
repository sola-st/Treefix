# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """
self._validate_inputs(self._input_tensors, self.quantized_input_stats)

quant_mode = QuantizationMode(
    self.optimizations, self.target_spec, self.representative_dataset,
    self._graph_def, self._experimental_disable_per_channel,
    self.experimental_new_dynamic_range_quantizer,
    self._experimental_low_bit_qat,
    self._experimental_full_integer_quantization_bias_type,
    self._experimental_variable_quantization)

optimized_graph = self._optimize_tf_model(self._graph_def,
                                          self._input_tensors,
                                          self._output_tensors, quant_mode)

self._debug_info = _get_debug_info(self._debug_info_func, optimized_graph)

converter_kwargs = self._get_base_converter_args()
converter_kwargs.update(
    quant_mode.converter_flags(self.inference_type,
                               self.inference_input_type))
converter_kwargs.update({
    "output_format": self.output_format,
    "quantized_input_stats": self._quantized_stats,
    "default_ranges_stats": self.default_ranges_stats,
    "drop_control_dependency": self.drop_control_dependency,
    "reorder_across_fake_quant": self.reorder_across_fake_quant,
    "change_concat_input_ranges": self.change_concat_input_ranges,
    "dump_graphviz_dir": self.dump_graphviz_dir,
    "dump_graphviz_video": self.dump_graphviz_video,
    "conversion_summary_dir": self.conversion_summary_dir,
})

self._validate_quantized_input_stats(converter_kwargs, quant_mode)
if not self.experimental_new_converter:
    logging.warning(
        "Please consider switching to the new converter by setting "
        "experimental_new_converter=True. "
        "The old converter is deprecated.")
else:
    logging.info("Using experimental converter: If you encountered a problem "
                 "please file a bug. You can opt-out "
                 "by setting experimental_new_converter=False")
# Converts model.
if self._has_valid_tensors():
    result = _convert_graphdef(
        input_data=optimized_graph,
        input_tensors=self._input_tensors,
        output_tensors=self._output_tensors,
        **converter_kwargs)
else:
    result = _convert_graphdef_with_arrays(
        input_data=optimized_graph,
        input_arrays_with_shape=self._input_arrays_with_shape,
        output_arrays=self._output_arrays,
        control_output_arrays=self._control_output_arrays,
        **converter_kwargs)

exit(self._optimize_tflite_model(
    result, quant_mode, quant_io=self.experimental_new_quantizer))
