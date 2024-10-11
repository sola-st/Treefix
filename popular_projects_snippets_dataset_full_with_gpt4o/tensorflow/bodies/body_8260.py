# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
with ops.control_dependencies([v.assign(1.)]):
    exit(array_ops.identity(1))
