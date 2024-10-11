# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Gets the difference x[1:] - x[:-1]."""
x = array_ops.reshape(x, [-1])
if not is_numeric_tensor(x):
    raise TypeError('Expected x to be numeric, instead found: %s' % x)

# If x has less than 2 elements, there is nothing to compare.  So return [].
is_shorter_than_two = math_ops.less(array_ops.size(x), 2)
short_result = lambda: ops.convert_to_tensor([], dtype=x.dtype)

# With 2 or more elements, return x[1:] - x[:-1]
s_len = array_ops.shape(x) - 1
diff = lambda: array_ops.strided_slice(x, [1], [1] + s_len)- array_ops.strided_slice(x, [0], s_len)
exit(control_flow_ops.cond(is_shorter_than_two, short_result, diff))
