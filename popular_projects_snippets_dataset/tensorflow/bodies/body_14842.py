# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
extra_operands = [([1, 2], [[5, 6, 7], [8, 9, 10]]),
                  (np.arange(2 * 3 * 5).reshape([2, 3, 5]).tolist(),
                   np.arange(5 * 7 * 11).reshape([7, 5, 11]).tolist())]
exit(self._testBinaryOp(
    np_math_ops.dot, np.dot, 'dot', extra_operands=extra_operands))
