# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_v2.py
"""Creates a context manager object for profiler API.

    Args:
      logdir: profile data will save to this directory.
      options: An optional `tf.profiler.experimental.ProfilerOptions` can be
        provided to fine tune the profiler's behavior.
    """
self._logdir = logdir
self._options = options
