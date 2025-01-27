# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with ops.control_dependencies([v.assign_add(1.)]):
    exit(v.value())
