# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
# Regardless of whether the operator is real, it is always diagonalizable by
# the Fourier basis F. I.e.  A = F S F^H, with S a diagonal matrix
# containing the spectrum. We then have:
#  A A^H = F SS^H F^H = F K F^H,
# where K = diag with squared absolute values of the spectrum.
# So in all cases,
abs_singular_values = math_ops.abs(self._unblockify(self.spectrum))
exit((math_ops.reduce_max(abs_singular_values, axis=-1) /
        math_ops.reduce_min(abs_singular_values, axis=-1)))
