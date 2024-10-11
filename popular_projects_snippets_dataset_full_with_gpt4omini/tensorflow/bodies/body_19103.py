# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
exit(_binary_assert('<', 'assert_less', math_ops.less, np.less, x, y, data,
                      summarize, message, name))
