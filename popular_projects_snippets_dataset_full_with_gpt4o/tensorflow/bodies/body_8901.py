# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
# The get should only return the closure with tag 2.
self.assertIs(closure2, queue.get(tag=2))
