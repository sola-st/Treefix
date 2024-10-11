# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
v = variable_scope.variable(
    1.0, name="foo", aggregation=variable_scope.VariableAggregation.SUM)
exit(v)
