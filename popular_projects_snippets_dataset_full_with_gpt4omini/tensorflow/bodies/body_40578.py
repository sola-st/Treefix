# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/profiler.py
"""Stop current profiling session and return its result.

  Returns:
    A binary string of tensorflow.tpu.Trace. User can write the string
    to file for offline analysis by tensorboard.

  Raises:
    ProfilerNotRunningError: If there is no active profiling session.
  """
global _profiler
global _run_num
with _profiler_lock:
    if _profiler is None:
        raise ProfilerNotRunningError(
            'Cannot stop profiling. No profiler is running.')
    if context.default_execution_mode == context.EAGER_MODE:
        context.context().executor.wait()
    result = _profiler.stop()
    _profiler = None
    _run_num += 1
exit(result)
