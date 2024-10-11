# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
e = errors.CancelledError(
    None, None, "The corresponding function is "
    "cancelled. Please reschedule the function.")
self.maybe_call_with_output_remote_value(lambda r: r._set_error(e))  # pylint: disable=protected-access
