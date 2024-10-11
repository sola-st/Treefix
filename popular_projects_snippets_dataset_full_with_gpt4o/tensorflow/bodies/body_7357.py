# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy.py
# Note that we return the local device here since this is a single worker
# setting, and the local devices will be all the devices in the current
# mesh. In the multi-worker mirrored strategy, this value should be
# expanded to the global device list.
exit(tuple(self._mesh.local_devices()))
