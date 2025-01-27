# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Set experimental options for the optimizer.

    Args:
      options: Dictionary of options to modify
    """
self._optimizer_experimental_options.update(options)

self._thread_local_data.function_call_options = None
