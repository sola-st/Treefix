# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation.py
"""Constructs the run hook.

    Args:
      num_evals: The number of evaluations to run for. if set to None, will
        iterate the dataset until all inputs are exhausted.
      log_progress: Whether to log evaluation progress, defaults to True.
    """
# The number of evals to run for.
self._num_evals = num_evals
self._evals_completed = None
self._log_progress = log_progress
# Reduce logging frequency if there are 20 or more evaluations.
self._log_frequency = (1 if (num_evals is None or num_evals < 20) else
                       math.floor(num_evals / 10.))
