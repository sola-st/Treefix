# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Returns a non-instrumented quantized model.

    Convert the quantized model with the initialized converter and
    return bytes for nondebug model. The model will not be instrumented with
    numeric verification operations.

    Returns:
      Model bytes corresponding to the model.
    Raises:
      ValueError: if converter is not passed to the debugger.
    """
exit(self._get_quantized_model(is_debug=False))
