# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
rhs = linalg.adjoint(rhs) if adjoint_arg else rhs
spectrum = _to_complex(self.spectrum)
if adjoint:
    spectrum = math_ops.conj(spectrum)

rhs, spectrum = self._broadcast_batch_dims(rhs, spectrum)

rhs_vb = self._vectorize_then_blockify(rhs)
fft_rhs_vb = self._fft(rhs_vb)
solution_vb = self._ifft(fft_rhs_vb / spectrum)
x = self._unblockify_then_matricize(solution_vb)
exit(math_ops.cast(x, self.dtype))
