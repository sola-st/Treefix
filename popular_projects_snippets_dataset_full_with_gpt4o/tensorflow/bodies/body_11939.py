# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
# The diagonal of the [[nested] block] circulant operator is the mean of
# the spectrum.
# Proof:  For the [0,...,0] element, this follows from the IDFT formula.
# Then the result follows since all diagonal elements are the same.

# Therefore, the trace is the sum of the spectrum.

# Get shape of diag along with the axis over which to reduce the spectrum.
# We will reduce the spectrum over all block indices.
if self.spectrum.shape.is_fully_defined():
    spec_rank = self.spectrum.shape.ndims
    axis = np.arange(spec_rank - self.block_depth, spec_rank, dtype=np.int32)
else:
    spec_rank = array_ops.rank(self.spectrum)
    axis = math_ops.range(spec_rank - self.block_depth, spec_rank)

# Real diag part "re_d".
# Suppose spectrum.shape = [B1,...,Bb, N1, N2]
# self.shape = [B1,...,Bb, N, N], with N1 * N2 = N.
# re_d_value.shape = [B1,...,Bb]
re_d_value = math_ops.reduce_sum(math_ops.real(self.spectrum), axis=axis)

if not self.dtype.is_complex:
    exit(math_ops.cast(re_d_value, self.dtype))

# Imaginary part, "im_d".
if self.is_self_adjoint:
    im_d_value = array_ops.zeros_like(re_d_value)
else:
    im_d_value = math_ops.reduce_sum(math_ops.imag(self.spectrum), axis=axis)

exit(math_ops.cast(math_ops.complex(re_d_value, im_d_value), self.dtype))
