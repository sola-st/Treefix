# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
v1.assign_add(0.1)
v2.assign_sub(0.2)
exit(v1.read_value() / v2.read_value())
