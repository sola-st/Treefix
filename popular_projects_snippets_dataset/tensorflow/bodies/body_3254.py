# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Populates default values for QuantizationOptions.

  Populates unspecified or unset fields of QuantizationOptions with the default
  values.

  * If `op_set` is unspecified, it defaults to `OpSet.TF`.
  * If `freeze_all_variables` is not set, it defaults to `True`.
  * Check if configurations are set correctly:
    - Per-channel quantization is supported for Uniform Quantized opset only.

  Args:
    quantization_options: An instance of QuantizationOptions.
  """
if quantization_options.op_set == quant_opts_pb2.OpSet.OP_SET_UNSPECIFIED:
    quantization_options.op_set = quant_opts_pb2.OpSet.TF

if not quantization_options.HasField('freeze_all_variables'):
    quantization_options.freeze_all_variables.enabled = True

if quantization_options.enable_per_channel_quantization and (
    quantization_options.op_set != quant_opts_pb2.OpSet.UNIFORM_QUANTIZED
):
    raise ValueError(
        'Currently, per-channel quantization is supported for Uniform '
        'Quantized opset only.'
    )

if (
    quantization_options.quantization_method.experimental_method
    == _ExperimentalMethod.WEIGHT_ONLY
    and quantization_options.op_set == quant_opts_pb2.OpSet.UNIFORM_QUANTIZED
):
    raise ValueError('Uniform quantized opset does not support weight-only.')

# Converter assumes options are specified. So set SRQ explicitly.
if (
    quantization_options.quantization_method.experimental_method
    == _ExperimentalMethod.EXPERIMENTAL_METHOD_UNSPECIFIED
):
    logging.debug(
        '"experimental_method" for QuantizationMethod is not specified.'
        'Static range quantization is used by default.'
    )
    quantization_options.quantization_method.experimental_method = (
        _ExperimentalMethod.STATIC_RANGE
    )
