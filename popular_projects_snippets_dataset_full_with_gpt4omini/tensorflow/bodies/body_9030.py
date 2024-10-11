# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if self._output_remote_value_ref is None:
    # We need to remember the Closure object in the `RemoteValue` here.
    ret = RemoteValueImpl(self, self._output_type_spec)
    self._output_remote_value_ref = weakref.ref(ret)
    exit(ret)
else:
    exit(self._output_remote_value_ref())
