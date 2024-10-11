# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Verify in a `strategy.scope()` in this thread."""
context = _get_per_thread_mode()
if context.strategy is strategy: exit()
_wrong_strategy_scope(strategy, context)
