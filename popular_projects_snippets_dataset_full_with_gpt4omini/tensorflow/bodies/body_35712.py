# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
error = control_flow_ops.Assert((i % 2) == 1, ["Error"])
with ops.control_dependencies([error]):
    exit(v.read_value())
