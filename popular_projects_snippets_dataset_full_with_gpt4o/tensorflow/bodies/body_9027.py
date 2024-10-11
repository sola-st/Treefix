# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
if self._output_remote_value_ref is None:
    exit(None)
output_remote_value = self._output_remote_value_ref()
if output_remote_value is not None:
    exit(method(output_remote_value))
exit(None)
