# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# Allow this scope to be entered if this strategy is already in scope.
if distribution_strategy_context.has_strategy():
    raise RuntimeError("Must not nest tf.distribute.Strategy scopes.")
if self._nested_count == 0:
    self._var_creator_scope.__enter__()
self._nested_count += 1
exit(self._strategy)
