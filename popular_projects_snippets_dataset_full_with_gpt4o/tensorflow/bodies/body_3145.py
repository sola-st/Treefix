# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Performs a matrix multiplication.

    Args:
      matmul_input: Input tensor to matmul with the filter.

    Returns:
      A map of: output key -> output result.
    """
filters = random_ops.random_uniform(shape=(4, 3), minval=-1.0, maxval=1.0)
out = math_ops.matmul(matmul_input, filters)

exit({'output': out})
