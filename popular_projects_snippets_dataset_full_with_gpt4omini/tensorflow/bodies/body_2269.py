# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
"""Tests broadcasting behavior of BatchMatMul."""
# [2, 3] @ [1, 3, 4] -> [1, 2, 4]
self._testBinary(
    math_ops.matmul,
    np.array([[10, 20, 30], [11, 21, 31]], dtype=np.float32),
    np.array([[[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]],
             dtype=np.float32),
    expected=np.array([[[140, 280, 420, 560], [146, 292, 438, 584]]],
                      dtype=np.float32))
# [1, 2, 3] @ [3, 4] -> [1, 2, 4]
self._testBinary(
    math_ops.matmul,
    np.array([[[10, 20, 30], [11, 21, 31]]], dtype=np.float32),
    np.array([[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]], dtype=np.float32),
    expected=np.array([[[140, 280, 420, 560], [146, 292, 438, 584]]],
                      dtype=np.float32))
# [2, 1, 3] @ [3, 1] -> [2, 1, 1]
self._testBinary(
    math_ops.matmul,
    np.array([[[10, 20, 30]], [[11, 21, 31]]], dtype=np.float32),
    np.array([[1], [2], [3]], dtype=np.float32),
    expected=np.array([[[140]], [[146]]], dtype=np.float32))
# [2, 1, 3] @ [1, 3] -> [2, 1, 1] (adjoint_b)
self._testBinary(
    lambda x, y: math_ops.matmul(x, y, adjoint_b=True),
    np.array([[[10, 20, 30]], [[11, 21, 31]]], dtype=np.float32),
    np.array([[1, 2, 3]], dtype=np.float32),
    expected=np.array([[[140]], [[146]]], dtype=np.float32))
# [2, 3, 1] @ [3, 1] -> [2, 1, 1] (adjoint_a)
self._testBinary(
    lambda x, y: math_ops.matmul(x, y, adjoint_a=True),
    np.array([[[10], [20], [30]], [[11], [21], [31]]], dtype=np.float32),
    np.array([[1], [2], [3]], dtype=np.float32),
    expected=np.array([[[140]], [[146]]], dtype=np.float32))
# [2, 3, 1] @ [1, 3] -> [2, 1, 1] (adjoint_a and adjoint_b)
self._testBinary(
    lambda x, y: math_ops.matmul(x, y, adjoint_a=True, adjoint_b=True),
    np.array([[[10], [20], [30]], [[11], [21], [31]]], dtype=np.float32),
    np.array([[1, 2, 3]], dtype=np.float32),
    expected=np.array([[[140]], [[146]]], dtype=np.float32))
# [5, 1, 2, 3] @ [1, 7, 3, 4] -> [5, 7, 2, 4]
self._testBinary(
    math_ops.matmul,
    np.ones([5, 1, 2, 3], dtype=np.float32),
    np.ones([1, 7, 3, 4], dtype=np.float32),
    expected=np.full([5, 7, 2, 4], 3, dtype=np.float32))
# [4, 5, 1, 2, 3] @ [1, 1, 3, 5] -> [4, 5, 1, 2, 5]
self._testBinary(
    math_ops.matmul,
    np.full([4, 5, 1, 2, 3], 2., dtype=np.float32),
    np.full([1, 1, 3, 5], 3., dtype=np.float32),
    expected=np.full([4, 5, 1, 2, 5], 18., dtype=np.float32))
