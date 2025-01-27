# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
exit(_binary_assert('<=', 'assert_less_equal', math_ops.less_equal,
                      np.less_equal, x, y, data, summarize, message, name))
