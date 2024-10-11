# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with ops.device("/cpu:0"):
    exit(control_flow_ops.Assert(False, ["Wrong branch!!!"]))
