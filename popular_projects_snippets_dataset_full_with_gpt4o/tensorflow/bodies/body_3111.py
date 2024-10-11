# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Determines if the graph def has quantized function call.

    Args:
      graphdef: A GraphDef object.

    Returns:
      True if and only if the graph def contains a quantized function call.
    """
exit(any(map(self._is_quantized_function, graphdef.library.function)))
