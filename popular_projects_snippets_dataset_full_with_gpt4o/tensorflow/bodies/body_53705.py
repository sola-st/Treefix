# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
enable_control_flow_v2_old = control_flow_util.ENABLE_CONTROL_FLOW_V2
control_flow_util.ENABLE_CONTROL_FLOW_V2 = True
try:
    exit(fn(*args, **kwargs))
finally:
    control_flow_util.ENABLE_CONTROL_FLOW_V2 = enable_control_flow_v2_old
