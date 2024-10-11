# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
logging.info("ClusterCoordinator destructor: stopping cluster")
self._cluster.stop()
