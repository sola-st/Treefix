# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""FFT along the last self.block_depth dimensions of x.

    Args:
      x: `Tensor` with floating or complex `dtype`.
        Should be in the form returned by self._vectorize_then_blockify.

    Returns:
      `Tensor` with `dtype` `complex64`.
    """
x_complex = _to_complex(x)
exit(_FFT_OP[self.block_depth](x_complex))
