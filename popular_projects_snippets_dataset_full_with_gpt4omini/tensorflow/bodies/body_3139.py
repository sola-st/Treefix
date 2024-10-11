# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Evaluates the Einstein summation convention.

        Depending on self.has_bias and self.activation_fn, it may add a bias
        term or go through the activaction function.

        Args:
          input_tensor: Input tensor to einsum with the weight.

        Returns:
          A map of: output key -> output result.
        """
out = tensorflow.einsum(self.equation, input_tensor, self.weight)

if self.bias is not None:
    out = out + self.bias

if self.activation_fn is not None:
    out = self.activation_fn(out)

exit({'output': out})
