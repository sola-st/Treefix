# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
"""Verifies the output values of the dilation function.

    Args:
      image: Input tensor with shape: [batch, in_height, in_width, channels].
      kernel: Filter tensor with shape: [filter_height, filter_width, channels].
      strides: Output strides, specified as [stride_height, stride_width].
      rates: Atrous rates, specified as [rate_height, rate_width].
      padding: Padding type.
      out: Expected output.
      use_gpu: Whether we are running on GPU.
    """
strides = [1] + strides + [1]
rates = [1] + rates + [1]

with self.cached_session(use_gpu=use_gpu):
    out_tensor = nn_ops.dilation2d(
        constant_op.constant(image, dtype=dtype),
        constant_op.constant(kernel, dtype=dtype),
        strides=strides,
        rates=rates,
        padding=padding,
        name="dilation2d")
    self.assertAllCloseAccordingToType(out, self.evaluate(out_tensor))
