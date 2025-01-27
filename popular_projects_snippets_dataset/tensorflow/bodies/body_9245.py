# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_v2.py
"""Start profiling TensorFlow performance.

  Args:
    logdir: Profiling results log directory.
    options: `ProfilerOptions` namedtuple to specify miscellaneous profiler
      options. See example usage below.

  Raises:
    AlreadyExistsError: If a profiling session is already running.

  Example usage:
  ```python
  options = tf.profiler.experimental.ProfilerOptions(host_tracer_level = 3,
                                                     python_tracer_level = 1,
                                                     device_tracer_level = 1)
  tf.profiler.experimental.start('logdir_path', options = options)
  # Training code here
  tf.profiler.experimental.stop()
  ```

  To view the profiling results, launch TensorBoard and point it to `logdir`.
  Open your browser and go to `localhost:6006/#profile` to view profiling
  results.

  """
global _profiler
with _profiler_lock:
    if _profiler is not None:
        raise errors.AlreadyExistsError(None, None,
                                        'Another profiler is running.')
    _profiler = _pywrap_profiler.ProfilerSession()
    try:
        # support for namedtuple in pybind11 is missing, we change it to
        # dict type first.
        opts = dict(options._asdict()) if options is not None else {}
        _profiler.start(logdir, opts)
    except errors.AlreadyExistsError:
        logging.warning('Another profiler session is running which is probably '
                        'created by profiler server. Please avoid using profiler '
                        'server and profiler APIs at the same time.')
        raise errors.AlreadyExistsError(None, None,
                                        'Another profiler is running.')
    except Exception:
        _profiler = None
        raise
