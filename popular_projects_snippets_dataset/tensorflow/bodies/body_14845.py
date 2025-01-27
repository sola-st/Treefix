# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
operands = [([[1, 2]], [[3, 4, 5], [6, 7, 8]])]
exit(self._testBinaryOp(
    np_math_ops.matmul, np.matmul, 'matmul', operands=operands))
