# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
previous_control_flow_v2_value = control_flow_util.ENABLE_CONTROL_FLOW_V2
control_flow_util.ENABLE_CONTROL_FLOW_V2 = True
return_value = control_flow_ops.cond(x < 50, lambda: x + 1, lambda: x * x)
control_flow_util.ENABLE_CONTROL_FLOW_V2 = previous_control_flow_v2_value
exit(return_value)
