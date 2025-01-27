# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Validate the input parameters.

    Args:
      graph_def: The TensorFlow GraphDef.
      input_tensors: List of input tensors.
    Raise:
      ValueError:
        Input shape is not specified.
        Invalid quantization parameters.
    """
# Update conversion params with graph_def.
self._save_conversion_params_metric(graph_def)
self._quant_mode = QuantizationMode(
    self.optimizations, self.target_spec, self.representative_dataset,
    graph_def, self._experimental_disable_per_channel,
    self.experimental_new_dynamic_range_quantizer,
    self._experimental_low_bit_qat,
    self._experimental_full_integer_quantization_bias_type,
    self._experimental_variable_quantization)
self._validate_inference_input_output_types(self._quant_mode)

if not self._is_unknown_shapes_allowed():
    # Checks dimensions in input tensor.
    for tensor in input_tensors:
        # Note that shape_list might be empty for scalar shapes.
        shape_list = tensor.shape.as_list()
        if None in shape_list[1:]:
            raise ValueError(
                "None is only supported in the 1st dimension. Tensor '{0}' has "
                "invalid shape '{1}'.".format(
                    _get_tensor_name(tensor), shape_list))
        elif shape_list and shape_list[0] is None:
            # Set the batch size to 1 if undefined.
            shape = tensor.shape.as_list()
            shape[0] = 1
            tensor.set_shape(shape)

if (self._trackable_obj is None or
    not hasattr(self._trackable_obj, "graph_debug_info")):
    self._debug_info = _get_debug_info(
        _build_debug_info_func(self._funcs[0].graph), graph_def)
else:
    self._debug_info = _get_debug_info(
        _convert_debug_info_func(self._trackable_obj.graph_debug_info),
        graph_def)
