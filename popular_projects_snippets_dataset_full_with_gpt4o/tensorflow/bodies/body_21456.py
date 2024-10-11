# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation.py
evals_completed = run_values.results['evals_completed']
if self._log_progress:
    if self._num_evals is None:
        logging.info('Evaluation [%d]', evals_completed)
    else:
        if ((evals_completed % self._log_frequency) == 0 or
            (self._num_evals == evals_completed)):
            logging.info('Evaluation [%d/%d]', evals_completed, self._num_evals)
if self._num_evals is not None and evals_completed >= self._num_evals:
    run_context.request_stop()
