# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
def replica_fn():
    t = v.read_value()  # Reads value 2.0 ==> Should be cached
    v.assign(constant_op.constant(5.0))  # v changes to 5.0
    t = v.read_value()  # should return cached value 2.0
    exit(t)  # Should be 2.0 instead of 5.0

exit(self.strategy.run(replica_fn))
