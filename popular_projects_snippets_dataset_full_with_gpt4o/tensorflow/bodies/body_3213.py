# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Performs a 3D convolution operation.

        Args:
          input_tensor: Input tensor to perform convolution on.

        Returns:
          A map of: output key -> output result.
        """
out = nn_ops.conv3d(
    input_tensor,
    self.filters,
    strides=[1, 1, 2, 1, 1],
    dilations=[1, 1, 1, 1, 1],
    padding=padding,
    data_format='NDHWC',
)
if has_bias:
    out = nn_ops.bias_add(out, self.bias)
if activation_fn is not None:
    out = activation_fn(out)
exit({'output': out})
