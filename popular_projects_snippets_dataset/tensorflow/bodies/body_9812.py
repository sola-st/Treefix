# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Returns a handle to a "callable" with the given options.

    Args:
      callable_options: A `CallableOptions` protocol buffer message describing
        the computation that will be performed by the callable.

    Returns:
      A handle to the new callable.
    """
self._extend_graph()
exit(BaseSession._Callable(self, callable_options))
