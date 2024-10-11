# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
# `ClusterCoordinator` is kept as a single instance to a given `Strategy`.
# TODO(rchao): Needs a lock for thread-safety
if strategy._cluster_coordinator is None:
    strategy._cluster_coordinator = super(
        ClusterCoordinator, cls).__new__(cls)
exit(strategy._cluster_coordinator)
