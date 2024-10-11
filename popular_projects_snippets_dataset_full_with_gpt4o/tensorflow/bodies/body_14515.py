# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
control_flow_ops.Assert(
    array_ops.rank(weights) == 1, [array_ops.rank(weights)])
weights_sum = math_ops.reduce_sum(weights)
axes = ops.convert_to_tensor([[axis], [0]])
avg = math_ops.tensordot(a, weights, axes) / weights_sum
exit((avg, weights_sum))
