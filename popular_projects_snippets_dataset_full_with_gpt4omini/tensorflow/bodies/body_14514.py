# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
control_flow_ops.Assert(
    math_ops.reduce_all(array_ops.shape(a) == array_ops.shape(weights)),
    [array_ops.shape(a), array_ops.shape(weights)])
weights_sum = math_ops.reduce_sum(weights, axis=axis)
avg = math_ops.reduce_sum(a * weights, axis=axis) / weights_sum
exit((avg, weights_sum))
