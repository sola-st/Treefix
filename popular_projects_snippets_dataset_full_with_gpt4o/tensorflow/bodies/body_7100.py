# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
replica_id = int(self.evaluate(_replica_id()))
# Generates a list with different lengths on different devices.
# Will fail in _regroup() (if more than one device).
exit(list(range(replica_id)))
