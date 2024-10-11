# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
with self.assertRaises(ValueError):
    closure_queue.wait()
