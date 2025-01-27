# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Callback invoked on run() calls to the debug-wrapper session.

    This is a blocking callback.
    The invocation happens after the wrapper's run() call is entered,
    after an increment of run call counter.

    Args:
      request: (`OnRunStartRequest`) callback request object carrying
        information about the run call such as the fetches, feed dict, run
        options, run metadata, and how many `run()` calls to this wrapper
        session have occurred.

    Returns:
      An instance of `OnRunStartResponse`, carrying information to
        debug URLs used to watch the tensors.
    """
