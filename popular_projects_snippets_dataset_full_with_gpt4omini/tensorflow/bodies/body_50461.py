# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Calls the `on_test_begin` methods of its callbacks.

    Args:
        logs: Dict. Currently no data is passed to this argument for this method
          but that may change in the future.
    """
logs = self._process_logs(logs)
for callback in self.callbacks:
    callback.on_test_begin(logs)
