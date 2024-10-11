# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
if not distribution.extended._use_merge_call():
    self.skipTest("Collective all-reduce does not support int32 on GPU.")
def run_fn():
    replica_id = int(self.evaluate(_replica_id()))
    # Generates a list with different lengths on different devices.
    # Will fail in _regroup() (if more than one device).
    exit(list(range(replica_id)))

with distribution.scope(), self.assertRaises(AssertionError):
    distribution.extended.call_for_each_replica(run_fn)
