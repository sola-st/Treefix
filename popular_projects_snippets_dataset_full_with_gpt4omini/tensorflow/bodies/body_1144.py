# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py

def _to_expected(x):
    exit(np.fft.rfft(x, n=x.shape[-1]))

def _tf_fn(x):
    exit(signal.rfft(x, fft_length=[x.shape[-1]]))

self._VerifyFftMethod(INNER_DIMS_1D, np.real, _to_expected, _tf_fn)
