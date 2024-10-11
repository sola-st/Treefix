# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
per_thread_mode = _get_per_thread_mode()
exit((per_thread_mode.strategy, per_thread_mode.replica_context))
