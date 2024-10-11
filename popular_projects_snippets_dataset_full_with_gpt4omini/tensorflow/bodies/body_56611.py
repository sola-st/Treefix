# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Convert the model and apply options.

    Converts the quantized model and initializes a quantized model interpreter
    with the quantized model. Returns a float model interpreter if float model
    is provided.

    Args:
      options: a QuantizationDebugOptions object.
      converter: an initialized tf.lite.TFLiteConverter.
      calibrated_model: Calibrated model bytes.
      float_model: Float model bytes.
    """
self.quant_model = convert.mlir_quantize(
    calibrated_model,
    disable_per_channel=converter._experimental_disable_per_channel,  # pylint: disable=protected-access
    fully_quantize=options.fully_quantize,
    enable_numeric_verify=True,
    denylisted_ops=options.denylisted_ops,
    denylisted_nodes=options.denylisted_nodes)
self._quant_interpreter = _interpreter.Interpreter(
    model_content=self.quant_model)
self._float_interpreter = None
if float_model is not None:
    self._float_interpreter = _interpreter.Interpreter(
        model_content=float_model)
