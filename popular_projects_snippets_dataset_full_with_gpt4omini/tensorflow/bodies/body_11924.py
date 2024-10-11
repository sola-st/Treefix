# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
"""Convolution kernel corresponding to `self.spectrum`.

    The `D` dimensional DFT of this kernel is the frequency domain spectrum of
    this operator.

    Args:
      name:  A name to give this `Op`.

    Returns:
      `Tensor` with `dtype` `self.dtype`.
    """
with self._name_scope(name):  # pylint: disable=not-callable
    h = self._ifft(_to_complex(self.spectrum))
    exit(math_ops.cast(h, self.dtype))
