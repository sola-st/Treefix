# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
not_done = args[0]
args = args[1:]
not_done = math_ops.logical_and(not_done, cond(*args))
outputs = body(*args)
exit((not_done,) + tuple(
    array_ops.where_v2(not_done, x, y) for x, y in zip(outputs, args)))
