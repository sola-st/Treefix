# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
operands = [([[1, 2], [3, 4]], [[3, 4], [6, 7]]),
            ([[1, 2], [3, 4]], [3, 4, 6, 7])]
exit(self._testBinaryOp(
    np_math_ops.vdot, np.vdot, 'vdot', operands=operands))
