# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
# The numpy version has strange result type when promotion happens,
# so set check_promotion_result_type to False.
exit(self._testBinaryOp(
    np_math_ops.minimum,
    np.minimum,
    'minimum',
    check_promotion_result_type=False))
