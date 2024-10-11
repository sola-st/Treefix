# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
with self.thread_coord.stop_on_exception():
    self._restart(downtime_secs, restart_job)
