# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Apply optimizations on a TFLite model."""

if quant_mode.is_integer_quantization():
    in_type, out_type = self.inference_input_type, self.inference_output_type

    if quant_mode.is_post_training_integer_quantization():
        q_in_type = in_type if in_type and quant_io else _dtypes.float32
        q_out_type = out_type if out_type and quant_io else _dtypes.float32
        q_activations_type = quant_mode.activations_type()
        q_bias_type = quant_mode.bias_type()
        q_allow_float = quant_mode.is_allow_float()
        q_variable_quantization = quant_mode.enable_mlir_variable_quantization
        model = self._quantize(model, q_in_type, q_out_type, q_activations_type,
                               q_bias_type, q_allow_float,
                               q_variable_quantization)

    m_in_type = in_type if in_type else _dtypes.float32
    m_out_type = out_type if out_type else _dtypes.float32
    # Skip updating model io types if MLIR quantizer already takes care of it
    if not (quant_mode.is_post_training_integer_quantization() and
            self.experimental_new_quantizer and quant_io and
            (m_in_type in [_dtypes.int8, _dtypes.uint8, _dtypes.float32]) and
            (m_out_type in [_dtypes.int8, _dtypes.uint8, _dtypes.float32])):
        model = _modify_model_io_type(model, m_in_type, m_out_type)

if self._sparsify_model():
    model = _mlir_sparsify(model)

try:
    model = _deduplicate_readonly_buffers(model)
except Exception:  # pylint: disable=broad-except
    # Skip buffer deduplication when flatbuffer library is not ready to be
    # utilized.
    logging.warning(
        "Buffer deduplication procedure will be skipped when flatbuffer "
        "library is not properly loaded")

exit(model)
