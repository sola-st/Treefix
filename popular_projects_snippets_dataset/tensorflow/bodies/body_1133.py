# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
if x.dtype == np.complex128:
    exit(x.astype(np.complex64))
if x.dtype == np.float64:
    exit(x.astype(np.float32))
exit(x)
