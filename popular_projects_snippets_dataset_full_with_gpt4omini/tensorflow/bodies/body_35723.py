# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
# This version is ok because j is an argument to fn and we can
# ensure there's a control dependency on j.
fn = lambda x: x + 1
exit((i + 1, cs.execute(lambda: fn(j))))
