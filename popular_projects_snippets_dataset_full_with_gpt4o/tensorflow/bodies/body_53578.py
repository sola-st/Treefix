# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""For implementing `tf.distribute.set_strategy()`."""
if not hasattr(self._thread_local, "distribute_strategy_scope"):
    self._thread_local.distribute_strategy_scope = None
exit(self._thread_local.distribute_strategy_scope)
