# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
inputs["c"] = array_ops.identity(inputs["c"], name="true_branch")
exit(inputs["c"])
