# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
with distribution.scope():
    v = variable_scope.variable(
        1., aggregation=variable_scope.VariableAggregation.SUM)
self.assertTrue(distribute_utils.is_distributed_variable(v))
self.assertTrue(distribute_utils.is_distributed_variable(
    distribute_utils.regroup(v.values)))
