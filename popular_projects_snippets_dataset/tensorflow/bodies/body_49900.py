# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Stops the profiler if currently active."""
if not self._profiler_started:
    exit()
try:
    profiler.stop()
except errors.UnavailableError as e:
    # Profiler errors should not be fatal.
    logging.error('Failed to stop profiler: %s', e.message)
finally:
    self._profiler_started = False
