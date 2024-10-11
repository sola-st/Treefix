# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Converts `input_data_str` to a TFLite model.

  Args:
    model_flags_str: Serialized proto describing model properties, see
      `model_flags.proto`.
    conversion_flags_str: Serialized proto describing conversion properties, see
      `toco/toco_flags.proto`.
    input_data_str: Input data in serialized form (e.g. a graphdef is common, or
      it can be hlo text or proto)
    debug_info_str: Serialized `GraphDebugInfo` proto describing logging
      information. (default None)
    enable_mlir_converter: Enables MLIR-based conversion. (default True)

  Returns:
    Converted model in serialized form (e.g. a TFLITE model is common).
  Raises:
    ConverterError: When conversion fails in TFLiteConverter, usually due to
      ops not being supported.
    RuntimeError: When conversion fails, an exception is raised with the error
      message embedded.
  """
# Historically, deprecated conversion failures would trigger a crash, so we
# attempt to run the converter out-of-process. The current MLIR conversion
# pipeline surfaces errors instead, and can be safely run in-process.
if enable_mlir_converter or not _deprecated_conversion_binary:
    try:
        model_str = wrap_toco.wrapped_toco_convert(model_flags_str,
                                                   conversion_flags_str,
                                                   input_data_str, debug_info_str,
                                                   enable_mlir_converter)
        exit(model_str)
    except Exception as e:
        converter_error = ConverterError(str(e))
        for error_data in _metrics_wrapper.retrieve_collected_errors():
            converter_error.append_error(error_data)
        raise converter_error

exit(_run_deprecated_conversion_binary(model_flags_str,
                                         conversion_flags_str, input_data_str,
                                         debug_info_str))
