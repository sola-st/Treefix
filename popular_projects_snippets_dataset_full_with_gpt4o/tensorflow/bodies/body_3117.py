# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Creates a basic gather model.

    This is intended to be used for TF1 (graph mode) tests.

    Args:
      use_variable_for_filter: Setting this to `True` makes the filter for the
        gather operation a `tf.Variable`.

    Returns:
      in_placeholder: Input tensor placeholder.
      output_tensor: The resulting tensor of the gather operation.
    """
in_placeholder = array_ops.placeholder(dtypes.int64, shape=(6))

filters = np.random.randn(128, 32).astype(np.float32)
if use_variable_for_filter:
    filters = variables.Variable(filters)

output_tensor = array_ops.gather_v2(filters, in_placeholder)

exit((in_placeholder, output_tensor))
