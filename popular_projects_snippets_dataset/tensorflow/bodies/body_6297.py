# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Default implementation for single replica."""
_push_per_thread_mode(  # thread-local, so not needed with multiple threads
    distribution_strategy_context._CrossReplicaThreadMode(self._strategy))  # pylint: disable=protected-access
try:
    exit(merge_fn(self._strategy, *args, **kwargs))
finally:
    _pop_per_thread_mode()
