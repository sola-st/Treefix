# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
self._VerifyFftMethod(INNER_DIMS_1D, lambda x: x, np.fft.ifft,
                      signal.ifft)
