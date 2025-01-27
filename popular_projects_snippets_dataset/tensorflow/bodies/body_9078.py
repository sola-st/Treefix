# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if isinstance(val, RemoteValue):
    exit(val.fetch())
else:
    exit(val)
