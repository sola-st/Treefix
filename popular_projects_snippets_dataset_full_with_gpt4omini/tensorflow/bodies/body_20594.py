# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster.py
if self._tf_cluster is not None:
    tf_cluster.TF_ShutdownCluster(self._tf_cluster)
    self._tf_cluster = None
