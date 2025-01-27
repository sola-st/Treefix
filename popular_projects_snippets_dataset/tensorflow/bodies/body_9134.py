# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
session_config = kwargs.get("session_config", None)
self._device_filters.extend(session_config.device_filters)
self._intra_op_parallelism_threads = (
    session_config.intra_op_parallelism_threads)
self._inter_op_parallelism_threads = (
    session_config.inter_op_parallelism_threads)
exit(MockServer())
