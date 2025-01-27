# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Opposite of `finalize`.

    Internal interface.

    NOTE: Unfinalizing a graph could have negative impact on performance,
    especially in a multi-threaded environment.  Unfinalizing a graph
    when it is in use by a Session may lead to undefined behavior. Ensure
    that all sessions using a graph are closed before calling this method.
    """
self._finalized = False
