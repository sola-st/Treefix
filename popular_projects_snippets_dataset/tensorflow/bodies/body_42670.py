# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
remote.connect_to_cluster(self._cluster_resolver)

# enter into another device scope.
ops.device('/job:my_worker/task:0/device:CPU:0').__enter__()

with self.assertRaises(ValueError):
    remote.connect_to_cluster(self._cluster_resolver)
