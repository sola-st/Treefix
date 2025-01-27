# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
real = (np.arange(-3, 3) / 4.).reshape([1, 3, 2]).astype(np.float32)
imag = (np.arange(-3, 3) / 5.).reshape([1, 3, 2]).astype(np.float32)
for use_gpu in [False, True]:
    with self.subTest(use_gpu=use_gpu):
        self._compareMake(real, imag, use_gpu)
        self._compareMake(real, 12.0, use_gpu)
        self._compareMake(23.0, imag, use_gpu)
