# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Exit the training loop by causing `should_stop()` to return `True`.

         Causes `step_fn` to exit by raising an exception.

      Raises:
        StopIteration
      """
raise StopIteration('step_fn has requested the iterations to stop.')
