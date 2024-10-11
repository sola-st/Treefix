# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
mean = math_ops.reduce_mean(x, [0])
var = math_ops.reduce_mean(math_ops.square(x - mean))  # biased var
rstd = math_ops.rsqrt(var + 1e-8)
exit((x - mean) * rstd)
