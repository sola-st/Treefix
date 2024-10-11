# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation.py
# Update number of steps to run in the first run call
if self._num_evals is None:
    steps = self._steps_per_run_initial_value
else:
    steps = min(self._steps_per_run_initial_value, self._num_evals)
self._steps_per_run_variable.load(steps, session=session)
