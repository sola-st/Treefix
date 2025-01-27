# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
self._VerifyFftMethod(INNER_DIMS_2D, lambda x: x, np.fft.fft2,
                      signal.fft2d)
