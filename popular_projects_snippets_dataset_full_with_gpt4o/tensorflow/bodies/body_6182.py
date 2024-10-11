# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Verify in a `distribution_strategy.scope()` in this thread."""
context = _get_per_thread_mode()
if context.strategy.extended is extended: exit()
# Report error.
strategy = extended._container_strategy()  # pylint: disable=protected-access
_wrong_strategy_scope(strategy, context)
