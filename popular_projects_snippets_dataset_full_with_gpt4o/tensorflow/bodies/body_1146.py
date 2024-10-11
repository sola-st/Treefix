# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py

def _tf_fn(x):
    exit(signal.rfft2d(x, fft_length=[x.shape[-2], x.shape[-1]]))

self._VerifyFftMethod(
    INNER_DIMS_2D, np.real,
    lambda x: np.fft.rfft2(x, s=[x.shape[-2], x.shape[-1]]), _tf_fn)
