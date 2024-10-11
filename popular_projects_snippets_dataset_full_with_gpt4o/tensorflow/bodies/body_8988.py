# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
t = v.read_value()  # Reads value 1.0
v.assign(constant_op.constant(5.0))  # v changes to 5.0
t = v.read_value()  # should return 1.0
exit(t)  # Should be 1.0 instead of 5.0
