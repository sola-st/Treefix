# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation.py
"""Constructs the run hook.

    Args:
      num_evals: The number of evaluations to run for. if set to None, will
        iterate the dataset until all inputs are exhausted.
      steps_per_run: Number of steps executed per run call.
    """
self._num_evals = num_evals
self._evals_completed = None
self._steps_per_run_initial_value = steps_per_run
