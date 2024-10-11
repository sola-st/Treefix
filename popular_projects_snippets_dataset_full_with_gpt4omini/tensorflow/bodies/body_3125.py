# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Performs a gather and a 2D convolution operation.

        Args:
          input_tensor: Input tensor to perform operation on.

        Returns:
          A map of: output key -> output result.
        """
conv_filters = np.random.uniform(
    low=-10, high=10, size=filter_shape
).astype('f4')

out = array_ops.gather_v2(self.embedding_w, input_tensor)
out = nn_ops.conv2d(
    out,
    conv_filters,
    strides=[1, 1, 2, 1],
    dilations=[1, 1, 1, 1],
    padding='SAME',
    data_format='NHWC',
)
exit({'output': out})
