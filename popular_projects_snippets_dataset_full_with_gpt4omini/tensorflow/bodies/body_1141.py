# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
self._VerifyFftMethod(INNER_DIMS_3D, lambda x: x,
                      lambda x: np.fft.ifftn(x, axes=(-3, -2, -1)),
                      signal.ifft3d, ATOL_3D, RTOL_3D)
