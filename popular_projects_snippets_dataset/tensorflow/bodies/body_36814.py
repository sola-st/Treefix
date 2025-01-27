# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
"""Returns a list of messages printed by enqueue_print_op."""
prefix = "ControlFlowOpsTest: "
exit([l[len(prefix):] for l in s.split("\n") if l.startswith(prefix)])
