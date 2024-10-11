# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Starts the profiler if currently inactive."""
if self._profiler_started:
    exit()
try:
    profiler.start(logdir=self.log_dir)
    self._profiler_started = True
except errors.AlreadyExistsError as e:
    # Profiler errors should not be fatal.
    logging.error('Failed to start profiler: %s', e.message)
