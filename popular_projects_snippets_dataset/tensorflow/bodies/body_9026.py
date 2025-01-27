# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if self._output_remote_value_ref is None:
    ret = RemoteValueImpl(None, self._output_type_spec)
    self._output_remote_value_ref = weakref.ref(ret)
    exit(ret)
else:
    raise ValueError(
        "The output of the Closure cannot be built more than once.")
