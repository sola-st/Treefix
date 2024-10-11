# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
x = np.random.rand(8, 4).astype("f")
self._testSliceMatrixDim0(x, 1, 2)
self._testSliceMatrixDim0(x, 3, 3)
y = np.random.rand(8, 7).astype("f")  # 7 * sizeof(float) is not aligned
self._testSliceMatrixDim0(y, 1, 2)
self._testSliceMatrixDim0(y, 3, 3)
