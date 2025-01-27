# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
exit(control_flow_ops.cond(pred, lambda: x, lambda: x + 1))
