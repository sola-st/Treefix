# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
# This version is ok because we manually add a control
# dependency on j, which is an argument to the while_loop body
# and captured by fn.
fn = lambda: j + 1
with ops.control_dependencies([j]):
    exit((i + 1, cs.execute(fn)))
