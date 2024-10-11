# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
class ConvModel(module.Module):
    """A simple model with a single conv2d, bias and relu."""

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(shape=input_shape, dtype=dtypes.float32)
        ]
    )
    def conv(self, input_tensor: core.Tensor) -> Mapping[str, core.Tensor]:
        """Performs a 2D convolution operation.

        Args:
          input_tensor: Input tensor to perform convolution on.

        Returns:
          A map of: output key -> output result.
        """
        filters = np.random.uniform(low=-10, high=10, size=filter_shape).astype(
            'f4'
        )
        out_channel_size = filter_shape[-1]
        bias = np.random.uniform(
            low=0, high=10, size=(out_channel_size)
        ).astype('f4')
        scale, offset = [1.0] * out_channel_size, [0.5] * out_channel_size
        mean, variance = scale, offset
        out = nn_ops.conv2d(
            input_tensor,
            filters,
            strides=[1, 1, 2, 1],
            dilations=[1, 1, 1, 1],
            padding='SAME',
            data_format='NHWC',
        )
        if has_bias:
            out = nn_ops.bias_add(out, bias, data_format='NHWC')
        if has_batch_norm:
            # Fusing is supported for non-training case.
            out, _, _, _, _, _ = nn_ops.fused_batch_norm_v3(
                out, scale, offset, mean, variance, is_training=False
            )
        if activation_fn is not None:
            out = activation_fn(out)
        exit({'output': out})

exit(ConvModel())
