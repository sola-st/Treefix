# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
ret = s.assign([[4, 4], [5, 5], [6, 6], [7, 7]])
with ops.control_dependencies([ret]):
    a = array_ops.ones((1, 1))
with ops.control_dependencies([control_flow_ops.group(ret)]):
    b = array_ops.ones((1, 1))
exit((a, b))
