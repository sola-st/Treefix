# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
shapes = [
    ([1, 3, 2], [1]),
    ([1, 3, 2], [2]),
    ([1, 3, 2], [3, 2]),
    ([1, 3, 2], [3, 1]),
    ([1, 3, 2], [1, 3, 2]),
    ([1, 3, 2], [2, 3, 1]),
    ([1, 3, 2], [2, 1, 1]),
    ([1, 3, 2], [1, 3, 1]),
    ([2, 1, 5], [2, 3, 1]),
    ([2, 0, 5], [2, 0, 1]),
    ([2, 3, 0], [2, 3, 1]),
]
for (xs, ys) in shapes:
    x = np.random.randint(0, 2, np.prod(xs)).astype(np.bool_).reshape(xs)
    y = np.random.randint(0, 2, np.prod(ys)).astype(np.bool_).reshape(ys)
    for use_gpu in [True, False]:
        with self.subTest(xs=xs, ys=ys, use_gpu=use_gpu):
            self._compareBinary(x, y, np.logical_and, math_ops.logical_and,
                                use_gpu)
            self._compareBinary(x, y, np.logical_or, math_ops.logical_or, use_gpu)
            self._compareBinary(x, y, np.logical_xor, math_ops.logical_xor,
                                use_gpu)
