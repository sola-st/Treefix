# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
ops.disable_eager_execution()
with self.assertRaises(ValueError):
    remote.connect_to_cluster(self._cluster_resolver)
ops.enable_eager_execution()
