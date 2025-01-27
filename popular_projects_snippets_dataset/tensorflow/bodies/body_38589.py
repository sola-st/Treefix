# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
vector = np.arange(0, 2).reshape((1, 1, 1, 2, 1))
self._compare(vector, use_gpu=False)
self._compare(vector, use_gpu=True)
