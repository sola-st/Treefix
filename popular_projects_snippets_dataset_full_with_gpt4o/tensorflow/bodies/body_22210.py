# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
if session_manager is None:
    self._session_manager = session_manager_mod.SessionManager(
        local_init_op=self._local_init_op,
        ready_op=self._ready_op,
        ready_for_local_init_op=self._ready_for_local_init_op,
        graph=self._graph,
        recovery_wait_secs=self._recovery_wait_secs,
        local_init_run_options=self._local_init_run_options)
else:
    self._session_manager = session_manager
