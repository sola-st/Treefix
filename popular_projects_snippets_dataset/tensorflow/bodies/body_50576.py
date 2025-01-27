# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Starts the profiler if currently inactive.

    Args:
      logdir: Directory where profiler results will be saved.
    """
if self._profiler_started:
    exit()
try:
    profiler.start(logdir=logdir)
    self._profiler_started = True
except errors.AlreadyExistsError as e:
    # Profiler errors should not be fatal.
    logging.error('Failed to start profiler: %s', e.message)
