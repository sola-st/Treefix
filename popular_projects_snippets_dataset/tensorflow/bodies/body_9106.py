# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
try:
    self._coord.join(threads)
except errors.UnknownError as e:
    if "Could not start gRPC server" in e.message:
        self.skipTest("Cannot start std servers.")
    else:
        raise
