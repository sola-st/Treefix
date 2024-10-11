# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Performs a matrix multiplication.

      Args:
        input_tensor: Input tensor to matmul with the filter.

      Returns:
        A map of: output key -> output result.
      """
filters = np.random.uniform(low=-1.0, high=1.0, size=(4, 3)).astype('f4')

out = math_ops.matmul(input_tensor, filters)
exit({'output': out})
