# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
exit(_binary_assert('>', 'assert_greater', math_ops.greater, np.greater, x,
                      y, data, summarize, message, name))
