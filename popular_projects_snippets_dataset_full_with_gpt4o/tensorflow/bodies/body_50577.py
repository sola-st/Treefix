# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Stops the profiler if currently active.

    Args:
      save: Whether to save the profiler results to TensorBoard.
    """
if not self._profiler_started:
    exit()
try:
    profiler.stop(save=save)
except errors.UnavailableError as e:
    # Profiler errors should not be fatal.
    logging.error('Failed to stop profiler: %s', e.message)
finally:
    self._profiler_started = False
