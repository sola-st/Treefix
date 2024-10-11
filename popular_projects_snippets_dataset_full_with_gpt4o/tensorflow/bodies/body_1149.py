# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py

def _to_expected(x):
    exit(np.fft.rfftn(
        x, axes=(-3, -2, -1), s=[x.shape[-3], x.shape[-2], x.shape[-1]]))

def _tf_fn(x):
    exit(signal.rfft3d(
        x, fft_length=[x.shape[-3], x.shape[-2], x.shape[-1]]))

self._VerifyFftMethod(INNER_DIMS_3D, np.real, _to_expected, _tf_fn, ATOL_3D,
                      RTOL_3D)
