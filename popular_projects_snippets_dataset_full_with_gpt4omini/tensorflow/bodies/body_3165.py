# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Performs a 2D convolution operation.

        Args:
          input_tensor: Input tensor to perform convolution on.

        Returns:
          A map of: output key -> output result.
        """
q_input = array_ops.fake_quant_with_min_max_args(
    input_tensor, min=-0.1, max=0.2, num_bits=8, narrow_range=False
)
filter_tensor = ops.convert_to_tensor(self.filter_value)
filter_min = array_ops.identity(
    array_ops.constant([-0.5, -0.5], dtype=dtypes.float32)
)
filter_max = array_ops.identity(
    array_ops.constant([0.5, 0.5], dtype=dtypes.float32)
)
q_filter = array_ops.fake_quant_with_min_max_vars_per_channel(
    filter_tensor, filter_min, filter_max, num_bits=8, narrow_range=True
)
bias = array_ops.constant([0.1, 0.2], dtype=dtypes.float32)
scale, offset = [1.0] * 2, [0.5] * 2
mean, variance = scale, offset
out = nn_ops.conv2d(
    q_input,
    q_filter,
    strides=[1, 1, 2, 1],
    dilations=[1, 1, 1, 1],
    padding='SAME',
    data_format='NHWC',
)
if has_bias:
    out = nn_ops.bias_add(out, bias, data_format='NHWC')
if activation_fn is not None:
    # The accuracy is not good when having FusedBatchNorm without
    # activation in this test.
    if has_batch_norm:
        # Fusing is supported for non-training case.
        out, _, _, _, _, _ = nn_ops.fused_batch_norm_v3(
            out, scale, offset, mean, variance, is_training=False
        )
    out = activation_fn(out)
out_min = array_ops.constant([-0.18, -0.32], dtype=dtypes.float32)
out_max = array_ops.constant([0.5, 0.5], dtype=dtypes.float32)
q_out = array_ops.fake_quant_with_min_max_vars_per_channel(
    out, min=out_min, max=out_max, num_bits=8, narrow_range=True
)
exit({'output': q_out})
