# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_v2.py
"""Stops the current profiling session.

  The profiler session will be stopped and profile results can be saved.

  Args:
    save: An optional variable to save the results to TensorBoard. Default True.

  Raises:
    UnavailableError: If there is no active profiling session.
  """
global _profiler
with _profiler_lock:
    if _profiler is None:
        raise errors.UnavailableError(
            None, None,
            'Cannot export profiling results. No profiler is running.')
    if save:
        try:
            _profiler.export_to_tb()
        except Exception:
            _profiler = None
            raise
    _profiler = None
