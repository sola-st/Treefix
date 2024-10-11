# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py

def _tf_fn(x):
    exit(signal.irfft2d(x, fft_length=[x.shape[-2], 2 * (x.shape[-1] - 1)]))

self._VerifyFftMethod(
    INNER_DIMS_2D,
    lambda x: np.fft.rfft2(np.real(x), s=[x.shape[-2], x.shape[-1]]),
    lambda x: np.fft.irfft2(x, s=[x.shape[-2], 2 * (x.shape[-1] - 1)]),
    _tf_fn)
