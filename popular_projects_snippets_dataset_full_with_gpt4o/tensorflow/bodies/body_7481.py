# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Simulates a cluster management system.

    - If auto_restart is True, it restarts processes that exit with a non-zero
      exit code. Note that when join() times out it overrides auto_restart to
      False.
    - If dependence_on_chief is True, it terminates all processes once the chief
      exits. If auto_restart is also True, it only terminates all processes if
      the chief exit with a zero exit code, otherwise it restarts the chief.

    This runs in self._watchdog_thread.
    """
while True:
    time.sleep(1)
    with self._process_lock:
        chief = self._processes.get(('chief', 0), None)
        # Terminate the cluster when _dependence_on_chief is True if either:
        # - chief has exited with zero exit code.
        # - chief has exited with non-zero exit code and self._auto_restart is
        #   False.
        if chief and self._dependence_on_chief and chief.exitcode is not None:
            if chief.exitcode == 0 or (not self._auto_restart):
                for p in self._processes.values():
                    # Give other processes a chance to exit on their own.
                    p.join(timeout=3)
                self._terminate_all()
                for p in self._processes.values():
                    p.join()
                exit()

        # Auto restart failed processes if self._auto_restart is True.
        if self._auto_restart:
            has_failure = False
            for (task_type, task_id), p in self._processes.items():
                if p.exitcode is not None and p.exitcode != 0:
                    has_failure = True
                    logging.info('Restarting failed %s-%d', task_type, task_id)
                    self._start_subprocess_and_reading_thread(task_type, task_id)
            if has_failure:
                continue

        # Exit the thread if all processes have exited at this point.
        if all(p.exitcode is not None for p in self._processes.values()):
            exit()
