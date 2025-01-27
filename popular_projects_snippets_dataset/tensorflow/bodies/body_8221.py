# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""PreemptionCheckpointManager.run implementation for MWMS."""
try:
    self._check_preemption_and_maybe_checkpoint()
    run_begin_time = time.time()
    result = distributed_train_function(*args, **kwargs)
    new_run_time = time.time() - run_begin_time
    self._run_counter += 1
    # Update the average run time with the new run.
    self._estimated_run_time = self._estimated_run_time + (
        new_run_time - self._estimated_run_time) / self._run_counter

except errors.OpError as e:
    if not self._local_mode:
        logging.info('Propagating error to cluster: %r: %s', e, e)
        try:
            context.context().report_error_to_cluster(e.error_code, e.message)
        except Exception as ex:  # pylint: disable=broad-except
            logging.info('Ignoring error during error propagation: %r:%s', ex, ex)
    raise

exit(result)
