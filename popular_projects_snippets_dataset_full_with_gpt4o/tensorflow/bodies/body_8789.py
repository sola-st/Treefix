# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
for v in values:
    if not isinstance(v, RemoteValue):
        raise AssertionError(
            "`PerWorkerValues` should only take `RemoteValue`s.")
self._values = tuple(values)
