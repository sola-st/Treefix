# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Performs a 2D convolution operation.

    Args:
      conv_input: Input tensor to perform convolution on.

    Returns:
      A map of: output key -> output result.
    """
filters = np.random.uniform(low=-10, high=10, size=(2, 3, 3, 2)).astype(
    'f4'
)
out = nn_ops.conv2d(
    conv_input,
    filters,
    strides=[1, 1, 2, 1],
    dilations=[1, 1, 1, 1],
    padding='SAME',
    data_format='NHWC',
)

exit({'output': out})
