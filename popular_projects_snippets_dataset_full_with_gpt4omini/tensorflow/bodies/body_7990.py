# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
ops.get_default_graph()._distribution_strategy_stack.pop(-1)  # pylint: disable=protected-access
