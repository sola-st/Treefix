# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py

def _restart_fn():
    with self.thread_coord.stop_on_exception():
        self._restart(downtime_secs, restart_job)

restart_thread = threading.Thread(target=_restart_fn)
restart_thread.start()
exit(restart_thread)
