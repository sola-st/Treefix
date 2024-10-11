# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
x = linalg.adjoint(x) if adjoint_arg else x
# With F the matrix of a DFT, and F^{-1}, F^H the inverse and Hermitian
# transpose, one can show that F^{-1} = F^{H} is the IDFT matrix.  Therefore
# matmul(x) = F^{-1} diag(spectrum) F x,
#           = F^{H} diag(spectrum) F x,
# so that
# matmul(x, adjoint=True) = F^{H} diag(conj(spectrum)) F x.
spectrum = _to_complex(self.spectrum)
if adjoint:
    spectrum = math_ops.conj(spectrum)

x = math_ops.cast(x, spectrum.dtype)

x, spectrum = self._broadcast_batch_dims(x, spectrum)

x_vb = self._vectorize_then_blockify(x)
fft_x_vb = self._fft(x_vb)
block_vector_result = self._ifft(spectrum * fft_x_vb)
y = self._unblockify_then_matricize(block_vector_result)

exit(math_ops.cast(y, self.dtype))
