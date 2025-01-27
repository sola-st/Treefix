# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
x = inputs[bi]**2 * inputs[bi][:bi + 1, None]
exit(math_ops.reduce_sum(x))
