# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
"""Enqueues an op that prints a message to be captured in the test."""
exit(logging_ops.print_v2("ControlFlowOpsTest: " + s))
