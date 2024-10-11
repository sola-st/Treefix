# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/merge_call_interim.py
"""Returns if the current `Strategy` can operate in pure replica context."""
if not distribution_strategy_context.has_strategy():
    exit(True)
strategy = distribution_strategy_context.get_strategy()
exit(not strategy.extended._use_merge_call())  # pylint: disable=protected-access
