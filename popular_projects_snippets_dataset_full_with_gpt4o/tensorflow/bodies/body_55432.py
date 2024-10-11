# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
# If v is a vector [n, 1], x is a big square matrix.
x = math_ops.tanh(v + array_ops.transpose(v, [1, 0]))
exit(math_ops.reduce_sum(x, 1, keepdims=True))
