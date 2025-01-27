# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform == "tpu":
    self.skipTest("TPU only supports 1D FFT")
shape = [2, 3, 4, 5]
rng = np.random.RandomState(0)
a = rng.randn(*shape) + 1.0j * rng.randn(*shape)
a = a.astype(np.complex64)
# FFT
c = self._NewComputation()
ops.Fft(ops.Constant(c, a), xla_client.FftType.FFT, shape[-3:])
self._ExecuteAndCompareClose(
    c, expected=[np.fft.fftn(a, axes=(1, 2, 3))], rtol=1e-4)
# IFFT
c = self._NewComputation()
ops.Fft(ops.Constant(c, a), xla_client.FftType.IFFT, shape[-3:])
self._ExecuteAndCompareClose(
    c, expected=[np.fft.ifftn(a, axes=(1, 2, 3))], rtol=1e-4)
# RFFT
b = rng.randn(*shape).astype(np.float32)
c = self._NewComputation()
ops.Fft(ops.Constant(c, b), xla_client.FftType.RFFT, shape[-3:])
self._ExecuteAndCompareClose(
    c, expected=[np.fft.rfftn(b, axes=(1, 2, 3))], rtol=1e-4)
# IRFFT
c = self._NewComputation()
ops.Fft(ops.Constant(c, a), xla_client.FftType.IRFFT, [3, 4, 8])
self._ExecuteAndCompareClose(
    c, expected=[np.fft.irfftn(a, axes=(1, 2, 3))], rtol=1e-4)
