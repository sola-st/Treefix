# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
exit(np.fft.rfftn(
    np.real(x),
    axes=(-3, -2, -1),
    s=[x.shape[-3] // 2, x.shape[-2], x.shape[-1] * 2]))
