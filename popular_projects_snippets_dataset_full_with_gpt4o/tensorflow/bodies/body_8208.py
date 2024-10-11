# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Makes configurations for using the handler with TPUStrategy."""
self._is_chief = True
self._poll_termination_signal_thread = None
self._cluster_wise_termination_watcher_thread = None
self._maybe_create_checkpoint_manager()
self._read_checkpoint_manager.restore_or_initialize()
self._run_counter = 0
