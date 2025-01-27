# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/profiler.py
"""Start profiling.

  Args:
    options: profiler options.

  Raises:
    ProfilerAlreadyRunningError: If another profiling session is running.
  """
global _profiler
with _profiler_lock:
    if _profiler is not None:
        raise ProfilerAlreadyRunningError('Another profiler is running.')
    if context.default_execution_mode == context.EAGER_MODE:
        context.ensure_initialized()
    _profiler = _pywrap_profiler.ProfilerSession()
    try:
        _profiler.start('', options if options is not None else {})
    except errors.AlreadyExistsError:
        logging.warning('Another profiler session is running which is probably '
                        'created by profiler server. Please avoid using profiler '
                        'server and profiler APIs at the same time.')
        raise ProfilerAlreadyRunningError('Another profiler is running.')
