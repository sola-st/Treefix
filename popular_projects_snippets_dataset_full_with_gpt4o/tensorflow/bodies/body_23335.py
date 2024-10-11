# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Returns a RewriterConfig proto for TRT transformation.

  Args:
    conversion_params: a TrtConversionParams instance.
    is_dynamic_op: whether to use dynamic engines.
    max_batch_size: maximum batch size for static engines.
    is_v2: whether we're getting a RewriterConfig for TF 2.0.
    disable_non_trt_optimizers: Turn off all default Grappler optimizers.
    use_implicit_batch: Whether to use implicit batch or explicit batch.
    profile_strategy: dynamic shape optimization profile strategy.

  Returns:
    A RewriterConfig proto which sets a TensorRTOptimizer to run Grappler.

  Raises:
    TypeError: if any of the parameters are of unexpected type.
    ValueError: if any of the parameters are of unexpected value.
  """
_check_conversion_params(conversion_params, is_v2=is_v2)
if is_v2 and is_dynamic_op is not None and not is_dynamic_op:
    raise ValueError("is_dynamic_op is either None or True for TF2")
if not is_v2 and is_dynamic_op is None:
    raise ValueError("is_dynamic_op can't be None for TF1")

if (is_dynamic_op is None or is_dynamic_op) and max_batch_size is not None:
    raise ValueError("max_batch_size has to be None for TF2"
                     " or when is_dynamic_op == True in TF1")
if is_dynamic_op is not None and not is_dynamic_op and not isinstance(
    max_batch_size, int):
    raise ValueError(
        "max_batch_size has to be an integer for is_dynamic_op==False in TF1")
rewriter_config_with_trt = rewriter_config_pb2.RewriterConfig()
# Disable Grappler Remapper to avoid that fused OPs that may not be
# beneficial to TF-TRT and are not supported by TF-TRT.
rewriter_config_with_trt.remapping = False

# Prevent folding of Const->QDQ chains.
rewriter_config_with_trt. \
    experimental_disable_folding_quantization_emulation = (
    trt_utils.is_linked_tensorrt_version_greater_equal(8, 0, 0) or
    trt_utils.is_loaded_tensorrt_version_greater_equal(8, 0, 0))

if not disable_non_trt_optimizers:
    rewriter_config_with_trt.optimizers.extend([
        "pruning", "debug_stripper", "layout", "dependency", "constfold",
        "common_subgraph_elimination"
    ])

rewriter_config_with_trt.meta_optimizer_iterations = (
    rewriter_config_pb2.RewriterConfig.ONE)
optimizer = rewriter_config_with_trt.custom_optimizers.add()

if not disable_non_trt_optimizers:
    # Add a constfold optimizer to cleanup the unused Const nodes.
    rewriter_config_with_trt.custom_optimizers.add().name = "constfold"

optimizer.name = "TensorRTOptimizer"
optimizer.parameter_map[
    "minimum_segment_size"].i = conversion_params.minimum_segment_size
optimizer.parameter_map["max_workspace_size_bytes"].i = (
    conversion_params.max_workspace_size_bytes)
optimizer.parameter_map["precision_mode"].s = _to_bytes(
    conversion_params.precision_mode)
optimizer.parameter_map[
    "maximum_cached_engines"].i = conversion_params.maximum_cached_engines
optimizer.parameter_map[
    "use_calibration"].b = conversion_params.use_calibration
optimizer.parameter_map["is_dynamic_op"].b = is_dynamic_op
optimizer.parameter_map[
    "allow_build_at_runtime"].b = conversion_params.allow_build_at_runtime
if max_batch_size is not None:
    optimizer.parameter_map["max_batch_size"].i = max_batch_size
optimizer.parameter_map["use_implicit_batch"].b = use_implicit_batch
# While we accept case insensitive strings from the users, we only pass the
# strings in lower cases to TF-TRT converter.
if not use_implicit_batch:
    optimizer.parameter_map["profile_strategy"].s = _to_bytes(
        profile_strategy.lower())

# Disabling optimizers should happen after defining the TF-TRT grappler pass
# otherwise the template can overwrite the disablement.
if disable_non_trt_optimizers:
    trt_utils.disable_non_trt_optimizers_in_rewriter_config(
        rewriter_config_with_trt)

exit(rewriter_config_with_trt)
