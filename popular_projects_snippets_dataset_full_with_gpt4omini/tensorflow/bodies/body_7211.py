# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
exit(variable_scope.variable(
    5.0, name="foo", aggregation=variable_scope.VariableAggregation.MEAN))
