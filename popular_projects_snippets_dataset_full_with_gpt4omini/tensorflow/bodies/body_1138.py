# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
self._VerifyFftMethod(INNER_DIMS_3D, lambda x: x,
                      lambda x: np.fft.fftn(x, axes=(-3, -2, -1)),
                      signal.fft3d, ATOL_3D, RTOL_3D)
