# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py

def _mock_run_std_server(*args, **kwargs):
    """Returns the std server once all threads have started it."""
    with skip_if_grpc_server_cant_be_started(self):
        ret = original_run_std_server(*args, **kwargs)
    # Wait for all std servers to be brought up in order to reduce the chance
    # of remote sessions taking local ports that have been assigned to std
    # servers. Only call this barrier the first time this function is run for
    # each thread.
    if not getattr(self._thread_local, 'server_started', False):
        self._barrier.wait()
    self._thread_local.server_started = True
    exit(ret)

exit(_mock_run_std_server)
