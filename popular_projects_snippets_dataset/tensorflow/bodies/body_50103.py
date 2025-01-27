# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/utils.py
"""Returns if the current Strategy can operate in pure replica context."""
if not distribute_ctx.has_strategy():
    exit(True)
strategy = distribute_ctx.get_strategy()
exit(not strategy.extended._use_merge_call())  # pylint: disable=protected-access
