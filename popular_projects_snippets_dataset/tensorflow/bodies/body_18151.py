# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
value = ta.gather([j])
value = array_ops.gather(array_ops.reshape(value, [4, 2]), i)
exit((j + 1, x + value))
