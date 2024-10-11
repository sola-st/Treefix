# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Runs the TFLite debugging model with given debug options.

    Args:
      quant_debug_model_path: Path to the quantized debug TFLite model file.
      quant_debug_model_content: Content of the quantized debug TFLite model.
      float_model_path: Path to float TFLite model file.
      float_model_content: Content of the float TFLite model.
      debug_dataset: a factory function that returns dataset generator which is
        used to generate input samples (list of np.ndarray) for the model. The
        generated elements must have same types and shape as inputs to the
        model.
      debug_options: Debug options to debug the given model.
      converter: Optional, use converter instead of quantized model.

    Raises:
      ValueError: If the debugger was unable to be created.

    Attributes:
      layer_statistics: results of error metrics for each NumericVerify op
        results. in {layer_name: {metric_name: metric}} format.
      model_statistics: results of error metrics for difference between float
        and quantized models. in {metric_name: metric} format.
    """
self._data_gen = debug_dataset
self._debug_options = debug_options or QuantizationDebugOptions()
self.converter = None
self.calibrated_model = None
self.float_model = None
self._float_interpreter = None
if converter is not None:
    if self._debug_options.model_debug_metrics:
        old_optimizations = converter.optimizations
        self.converter = self._set_converter_options_for_float(converter)
        self.float_model = self.converter.convert()
        converter.optimizations = old_optimizations

    self.converter = self._set_converter_options_for_calibration(converter)
    self.calibrated_model = self.converter.convert()
    # Converter should be already set up with all options
    self._init_from_converter(
        self._debug_options,
        self.converter,
        self.calibrated_model,
        float_model=self.float_model)
else:
    self._quant_interpreter = _interpreter.Interpreter(
        quant_debug_model_path,
        quant_debug_model_content,
        experimental_preserve_all_tensors=(
            self._debug_options.layer_direct_compare_metrics is not None))
    if self._debug_options.model_debug_metrics:
        self._float_interpreter = _interpreter.Interpreter(
            float_model_path, float_model_content)
self._initialize_stats()
