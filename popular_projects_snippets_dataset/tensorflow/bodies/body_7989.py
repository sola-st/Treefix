# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
ops.get_default_graph()._distribution_strategy_stack.append(context)  # pylint: disable=protected-access
