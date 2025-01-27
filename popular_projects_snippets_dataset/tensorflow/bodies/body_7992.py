# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
try:
    exit(ops.get_default_graph()._distribution_strategy_stack[-1])  # pylint: disable=protected-access
except (AttributeError, IndexError):
    exit(_get_default_replica_mode())
