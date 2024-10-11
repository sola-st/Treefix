# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Builds protocol buffer describing a conversion of a model.

  Typically this is to convert from TensorFlow GraphDef to TFLite, in which
  case the default `input_format` and `output_format` are sufficient.

  Args:
    inference_type: Data type of numeric arrays, excluding the input layer.
      (default tf.float32, must be in {tf.float32, tf.int8, tf.uint8})
    inference_input_type: Data type of the numeric arrays in the input layer. If
      `inference_input_type` is in {tf.int8, tf.uint8}, then
      `quantized_input_stats` must be provided. (default is the value assigned
      to `inference_type`, must be in {tf.float32, tf.int8, tf.uint8})
    input_format: Type of data to read. (default TENSORFLOW_GRAPHDEF, must be in
      {TENSORFLOW_GRAPHDEF})
    output_format: Output file format. (default TFLITE, must be in {TFLITE,
      GRAPHVIZ_DOT})
    default_ranges_stats: Tuple of integers representing (min, max) range values
      for all arrays without a specified range. Intended for experimenting with
      quantization via "dummy quantization". (default None)
    drop_control_dependency: Boolean indicating whether to drop control
      dependencies silently. This is due to TFLite not supporting control
      dependencies. (default True)
    reorder_across_fake_quant: Boolean indicating whether to reorder FakeQuant
      nodes in unexpected locations. Used when the location of the FakeQuant
      nodes is preventing graph transformations necessary to convert the graph.
      Results in a graph that differs from the quantized training graph,
      potentially causing differing arithmetic behavior. (default False)
    allow_custom_ops: Boolean indicating whether to allow custom operations.
      When false any unknown operation is an error. When true, custom ops are
      created for any op that is unknown. The developer will need to provide
      these to the TensorFlow Lite runtime with a custom resolver. (default
      False)
    post_training_quantize: Boolean indicating whether to quantize the weights
      of the converted float model. Model size will be reduced and there will be
      latency improvements (at the cost of accuracy). (default False)
    quantize_to_float16: Boolean indicating whether to convert float buffers to
      float16. (default False)
    dump_graphviz_dir: Full filepath of folder to dump the graphs at various
      stages of processing GraphViz .dot files. Preferred over
      --output_format=GRAPHVIZ_DOT in order to keep the requirements of the
      output file. (default None)
    dump_graphviz_video: Boolean indicating whether to dump the graph after
      every graph transformation. (default False)
    target_ops: Experimental flag, subject to change. Set of OpsSet options
      indicating which converter to use. (default set([OpsSet.TFLITE_BUILTINS]))
    conversion_summary_dir: A string, the path to the generated conversion logs.
    select_user_tf_ops: List of user's defined TensorFlow ops need to be
      supported in the TensorFlow Lite runtime. These ops will be supported as
      select TensorFlow ops.
    allow_all_select_tf_ops: If True, automatically add all TF ops (including
      custom TF ops) to the converted model as flex ops.
    enable_tflite_resource_variables: Experimental flag, subject to change.
      Enables conversion of resource variables. (default False)
    unfold_batchmatmul: Whether to unfold tf.BatchMatMul to a set of
      tfl.fully_connected ops. If not, translate to tfl.batch_matmul.
    lower_tensor_list_ops: Whether to lower tensor list ops to builtin ops. If
      not, use Flex tensor list ops.
    default_to_single_batch_in_tensor_list_ops: Whether to force to use batch
      size one when the tensor list ops has the unspecified batch size.
    accumulation_type: Data type of the accumulators in quantized inference.
      Typically used for float16 quantization and is either fp16 or fp32.
    allow_bfloat16: Whether the converted model supports reduced precision
      inference with the bfloat16 type.
    unfold_large_splat_constant: Whether to unfold large splat constant tensors
      in the flatbuffer model to reduce size.
    supported_backends: List of TFLite backends which needs to check
      compatibility.
    disable_per_channel_quantization: Disable per-channel quantized weights for
      dynamic range quantization. Only per-tensor quantization will be used.
    enable_mlir_dynamic_range_quantizer: Enable MLIR dynamic range quantization.
      If False, the old converter dynamic range quantizer is used.
    tf_quantization_mode: Indicates the mode of TF Quantization when the output
      model is used for TF Quantization.
    disable_infer_tensor_range: Disable infering tensor ranges.
    use_fake_quant_num_bits: Allow quantization parameters to be calculated from
      num_bits attribute.
    enable_dynamic_update_slice: Enable to convert to DynamicUpdateSlice op.
      (default: False).
    preserve_assert_op: Whether to preserve `TF::AssertOp` (default: False).
    guarantee_all_funcs_one_use: Whether to clone functions so that each
      function only has a single use. This option will be helpful if the
      conversion fails when the `PartitionedCall` or `StatefulPartitionedCall`
      can't be properly inlined (default: False).
    enable_mlir_variable_quantization: Enable MLIR variable quantization. There
      is a variable freezing pass, but some variables may not be fully frozen by
      it. This flag enables quantization of those residual variables in the MLIR
      graph.

  Returns:
    conversion_flags: protocol buffer describing the conversion process.
  Raises:
    ValueError, if the input tensor type is unknown.
  """
conversion_flags = _conversion_flags_pb2.TocoFlags()
conversion_flags.inference_type = convert_inference_tf_type_to_tflite_type(
    inference_type, usage="inference_type flag")
if inference_input_type:
    conversion_flags.inference_input_type = (
        convert_inference_tf_type_to_tflite_type(
            inference_input_type, usage="inference_input_type flag"))
else:
    conversion_flags.inference_input_type = conversion_flags.inference_type
conversion_flags.input_format = input_format
conversion_flags.output_format = output_format
if default_ranges_stats:
    conversion_flags.default_ranges_min = default_ranges_stats[0]
    conversion_flags.default_ranges_max = default_ranges_stats[1]
conversion_flags.drop_control_dependency = drop_control_dependency
conversion_flags.reorder_across_fake_quant = reorder_across_fake_quant
conversion_flags.allow_custom_ops = allow_custom_ops
conversion_flags.post_training_quantize = post_training_quantize
conversion_flags.quantize_to_float16 = quantize_to_float16
if dump_graphviz_dir:
    conversion_flags.dump_graphviz_dir = dump_graphviz_dir
conversion_flags.dump_graphviz_include_video = dump_graphviz_video
if target_ops:
    if OpsSet.SELECT_TF_OPS in target_ops:
        conversion_flags.enable_select_tf_ops = True
    if set(target_ops) == {OpsSet.SELECT_TF_OPS}:
        conversion_flags.force_select_tf_ops = True
    if OpsSet.EXPERIMENTAL_STABLEHLO_OPS in target_ops:
        conversion_flags.convert_to_stablehlo = True
    if OpsSet.EXPERIMENTAL_STABLEHLO_OPS in target_ops and len(target_ops) > 1:
        raise ValueError("StableHLO Ops set can not be specified with other Ops "
                         "set together")
if conversion_summary_dir:
    conversion_flags.conversion_summary_dir = conversion_summary_dir
if select_user_tf_ops:
    conversion_flags.select_user_tf_ops.extend(select_user_tf_ops)
conversion_flags.allow_all_select_tf_ops = allow_all_select_tf_ops
conversion_flags.enable_tflite_resource_variables = (
    enable_tflite_resource_variables)
conversion_flags.unfold_batchmatmul = unfold_batchmatmul
conversion_flags.lower_tensor_list_ops = lower_tensor_list_ops
conversion_flags.default_to_single_batch_in_tensor_list_ops = (
    default_to_single_batch_in_tensor_list_ops)
if accumulation_type:
    conversion_flags.accumulation_type = convert_tensor_tf_type_to_tflite_type(
        accumulation_type, usage="accumulation_type flag")
conversion_flags.allow_bfloat16 = allow_bfloat16
conversion_flags.unfold_large_splat_constant = unfold_large_splat_constant
if supported_backends:
    conversion_flags.supported_backends.extend(supported_backends)
conversion_flags.disable_per_channel_quantization = (
    disable_per_channel_quantization)
conversion_flags.enable_mlir_dynamic_range_quantizer = (
    enable_mlir_dynamic_range_quantizer)
conversion_flags.enable_dynamic_update_slice = enable_dynamic_update_slice
conversion_flags.preserve_assert_op = preserve_assert_op
conversion_flags.guarantee_all_funcs_one_use = guarantee_all_funcs_one_use
if tf_quantization_mode:
    conversion_flags.tf_quantization_mode = tf_quantization_mode
conversion_flags.disable_infer_tensor_range = disable_infer_tensor_range
conversion_flags.use_fake_quant_num_bits = use_fake_quant_num_bits
conversion_flags.enable_mlir_variable_quantization = (
    enable_mlir_variable_quantization)
exit(conversion_flags)
