# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
exit(_binary_assert('!=', 'assert_none_equal', math_ops.not_equal,
                      np.not_equal, x, y, data, summarize, message, name))
