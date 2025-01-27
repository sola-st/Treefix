# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Convert a frozen GraphDef model using the TF Lite converter.

  Conversion can be customized by providing arguments that are forwarded to
  `build_model_flags` and `build_conversion_flags` (see documentation).

  Args:
    input_data: Input data (i.e. often `sess.graph_def`),
   input_tensors: List of input tensors. Type and shape are computed using
     `foo.shape` and `foo.dtype`.
    output_tensors: List of output tensors (only .name is used from this).
    **kwargs: See `build_model_flags` and `build_conversion_flags`.

  Returns:
    The converted data. For example if TFLite was the destination, then
    this will be a tflite flatbuffer in a bytes array.

  Raises:
    Defined in `build_conversion_flags`.
  """
model_flags = build_model_flags(**kwargs)
conversion_flags = build_conversion_flags(**kwargs)
saved_model_dir = kwargs.get("saved_model_dir", None)
input_shapes = kwargs.get("input_shapes", None)
enable_mlir_converter = kwargs.get("enable_mlir_converter", True)
quantized_input_stats = kwargs.get("quantized_input_stats", None)
debug_info = kwargs.get("debug_info", None)

for idx, input_tensor in enumerate(input_tensors):
    input_array = model_flags.input_arrays.add()
    if saved_model_dir:
        input_array.name = input_tensor.name
    else:
        input_array.name = util.get_tensor_name(input_tensor)
    input_array.data_type = convert_tensor_tf_type_to_tflite_type(
        input_tensor.dtype, usage="input type of the TensorFlow model")

    if _is_quantized_input_stats_required(conversion_flags):
        if quantized_input_stats:
            input_array.mean_value, input_array.std_value = (
                quantized_input_stats[idx])
        else:
            # We should ideally raise an error here, but we don't as it would break
            # several models/projects that depend on this workflow.
            warnings.warn("Statistics for quantized inputs were expected, but not "
                          "specified; continuing anyway.")

    if input_shapes is None:
        shape = input_tensor.shape
    else:
        shape = input_shapes[idx]

    if shape.rank is not None:
        # Create shapes with -1 for unknown dimensions.
        dims = []
        for dim in shape:
            if (dim is None or
                (isinstance(dim, tensor_shape.Dimension) and dim.value is None)):
                dims.append(-1)
            else:
                dims.append(int(dim))
        input_array.shape.dims.extend(dims)
        input_array.shape.unknown_rank = False
    else:
        input_array.shape.unknown_rank = True

for output_tensor in output_tensors:
    if saved_model_dir:
        model_flags.output_arrays.append(output_tensor.name)
    else:
        model_flags.output_arrays.append(util.get_tensor_name(output_tensor))

data = convert(
    model_flags.SerializeToString(),
    conversion_flags.SerializeToString(),
    input_data.SerializeToString(),
    debug_info_str=debug_info.SerializeToString() if debug_info else None,
    enable_mlir_converter=enable_mlir_converter)
exit(data)
