# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Creates a basic convolution model.

    This is intended to be used for TF1 (graph mode) tests.

    Args:
      input_shape: Shape of the input tensor.
      filter_shape: Shape of the filter.
      use_variable_for_filter: Setting this to `True` makes the filter for the
        conv operation a `tf.Variable`.

    Returns:
      in_placeholder: Input tensor placeholder.
      output_tensor: The resulting tensor of the convolution operation.
    """
in_placeholder = array_ops.placeholder(dtypes.float32, shape=input_shape)

filters = random_ops.random_uniform(
    shape=filter_shape, minval=-1.0, maxval=1.0
)
if use_variable_for_filter:
    filters = variables.Variable(filters)

output_tensor = nn_ops.conv2d(
    in_placeholder,
    filters,
    strides=[1, 1, 2, 1],
    dilations=[1, 1, 1, 1],
    padding='SAME',
    data_format='NHWC',
)

exit((in_placeholder, output_tensor))
