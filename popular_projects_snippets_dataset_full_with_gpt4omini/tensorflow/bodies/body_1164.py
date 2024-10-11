# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py

def _to_input(x):
    exit(np.fft.rfftn(
        np.real(x),
        axes=(-3, -2, -1),
        s=[x.shape[-3] // 2, x.shape[-2], x.shape[-1] * 2]))

def _to_expected(x):
    exit(np.fft.irfftn(
        x,
        axes=(-3, -2, -1),
        s=[x.shape[-3] // 2, x.shape[-2], x.shape[-1] * 2]))

def _tf_fn(x):
    exit(signal.irfft3d(
        x, fft_length=[x.shape[-3] // 2, x.shape[-2], x.shape[-1] * 2]))

self._VerifyFftMethod(INNER_DIMS_3D, _to_input, _to_expected, _tf_fn,
                      ATOL_3D, RTOL_3D)
