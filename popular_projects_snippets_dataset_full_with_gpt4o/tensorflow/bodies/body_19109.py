# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
exit(_binary_assert('>=', 'assert_greater_equal', math_ops.greater_equal,
                      np.greater_equal, x, y, data, summarize, message, name))
