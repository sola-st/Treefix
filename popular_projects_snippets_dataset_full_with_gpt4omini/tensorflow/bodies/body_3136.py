# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Performs a matrix multiplication.

        Depending on self.has_bias and self.activation_fn, it may add a bias
        term or
        go through the activaction function.

        Args:
          input_tensor: Input tensor to matmul with the filter.

        Returns:
          A map of: output key -> output result.
        """
out = math_ops.matmul(input_tensor, self.filters)

if self.has_bias:
    out = nn_ops.bias_add(out, self.bias)

if self.activation_fn is not None:
    out = self.activation_fn(out)

exit({'output': out})
