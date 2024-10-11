# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py

def _tf_fn(x):
    exit(signal.irfft(x, fft_length=[2 * (x.shape[-1] - 1)]))

self._VerifyFftMethod(
    INNER_DIMS_1D, lambda x: np.fft.rfft(np.real(x), n=x.shape[-1]),
    lambda x: np.fft.irfft(x, n=2 * (x.shape[-1] - 1)), _tf_fn)
