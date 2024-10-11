# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation.py
evals_completed = run_values.results['evals_completed']
# Update number of steps to run in the next iteration
if self._num_evals is None:
    steps = self._steps_per_run_initial_value
else:
    steps = min(self._num_evals - evals_completed,
                self._steps_per_run_initial_value)
self._steps_per_run_variable.load(steps, session=run_context.session)

if self._num_evals is None:
    logging.info('Evaluation [%d]', evals_completed)
else:
    logging.info('Evaluation [%d/%d]', evals_completed, self._num_evals)
if self._num_evals is not None and evals_completed >= self._num_evals:
    run_context.request_stop()
