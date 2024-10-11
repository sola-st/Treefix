# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/trace.py
"""Creates a trace event in the profiler.

    Args:
      name: The name of the trace event.
      **kwargs: Keyword arguments added to the trace event.
                Both the key and value are of types that
                can be converted to strings, which will be
                interpreted by the profiler according to the
                traceme name.

      Example usage:

      ```python

        tf.profiler.experimental.start('logdir')
        for step in range(num_steps):
          # Creates a trace event for each training step with the
          # step number.
          with tf.profiler.experimental.Trace("Train", step_num=step):
            train_fn()
        tf.profiler.experimental.stop()

      ```
      The example above uses the keyword argument "step_num" to specify the
      training step being traced.
    """
if enabled:
    # Creating _pywrap_traceme.TraceMe starts the clock.
    self._traceme = _pywrap_traceme.TraceMe(name, **kwargs)
else:
    self._traceme = None
