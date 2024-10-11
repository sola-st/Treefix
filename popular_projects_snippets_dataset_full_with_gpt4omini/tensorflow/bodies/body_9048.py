# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""A loop that handles preemption.

    This loop waits for signal of worker preemption and upon worker preemption,
    it waits until all workers are back and updates the cluster about the
    restarted workers.
    """
assert self._should_preemption_thread_run
while True:
    self._cluster_due_for_update_or_finish.wait()
    if not self._should_preemption_thread_run:
        logging.info("Stopping the failure handing thread.")
        break

    with self._cluster_update_lock:
        try:
            # TODO(haoyuzhang): support partial cluster recovery
            logging.info("Cluster now being recovered.")
            with metric_utils.monitored_timer("server_def_update"):
                context.context().update_server_def(self._server_def)

            # Cluster updated successfully, clear the update signal, and notify
            # all workers that they are recovered from failure.
            logging.info("Cluster successfully recovered.")
            self._worker_up_cond.notify_all()
            # The check for _should_preemption_thread_run is necessary since the
            # `stop` may have already set _cluster_due_for_update_or_finish.
            if self._should_preemption_thread_run:
                self._cluster_due_for_update_or_finish.clear()
        except Exception as e:  # pylint: disable=broad-except
            logging.info("Error occurred while updating server def: %s", e)
            try:
                self._validate_preemption_failure(e)
            except Exception as ps_e:  # pylint: disable=broad-except
                logging.info("Error that occurred while updating server def is not "
                             "a worker failure. So set it as _error_from_recovery")
                # In this case, a parameter server fails. So we raise this error to
                # the caller of `wait_on_failure`.
                self._error_from_recovery = ps_e
                self._worker_up_cond.notify_all()
                if self._should_preemption_thread_run:
                    self._cluster_due_for_update_or_finish.clear()
          # NOTE: Since the first RPC (GetStatus) of update_server_def is
          # currently blocking by default, error should only happen if:
          # (1) More workers failed while waiting for the previous workers to
          #     come back;
          # (2) Worker failed when exchanging subsequent RPCs after the first
          #     RPC returns.
          # Consider adding backoff retry logic if we see the error logged
          # too frequently.
            logging.error("Cluster update failed with error: %s. Retrying...", e)
