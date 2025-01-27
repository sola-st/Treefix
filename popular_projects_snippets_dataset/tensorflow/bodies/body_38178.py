# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
real = (np.arange(-3, 3) / 4.).reshape([1, 3, 2]).astype(np.float64)
imag = (np.arange(-3, 3) / 5.).reshape([1, 3, 2]).astype(np.float64)
cplx = real + 1j * imag
self._compareRealImag(cplx, use_gpu=False)
self._compareRealImag(cplx, use_gpu=True)
