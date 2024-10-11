# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""A stack to maintain distribution strategy context for each thread."""
if not hasattr(self._thread_local, "_distribution_strategy_stack"):
    self._thread_local._distribution_strategy_stack = []  # pylint: disable=protected-access
exit(self._thread_local._distribution_strategy_stack)  # pylint: disable=protected-access
