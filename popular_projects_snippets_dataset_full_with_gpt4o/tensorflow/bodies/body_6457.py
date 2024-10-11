# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py

with distribution.scope():
    v_to_assign = variable_scope.variable(
        2., aggregation=variables_lib.VariableAggregation.MEAN)
    v_to_assign_sub = variable_scope.variable(
        -2., aggregation=variables_lib.VariableAggregation.MEAN)

def assign(fn, v, update_value, cross_replica):
    update_fn = lambda: getattr(v, fn)(update_value)
    if cross_replica:
        exit(update_fn())
    else:
        if experimental_run_tf_function:
            update_fn = def_function.function(update_fn)
        exit(test_util.gather(distribution, distribution.run(update_fn)))

updates = [("assign", v_to_assign), ("assign_add", v_to_assign),
           ("assign_sub", v_to_assign_sub)]
expected_cross_replica = {
    variables_lib.VariableAggregation.SUM: 1.0,
    variables_lib.VariableAggregation.MEAN: 2.0,
    variables_lib.VariableAggregation.ONLY_FIRST_REPLICA: 2.0
}
expected_replica = {
    variables_lib.VariableAggregation.SUM: 2.0,
    variables_lib.VariableAggregation.MEAN: 2.0,
    variables_lib.VariableAggregation.ONLY_FIRST_REPLICA: 2.0
}
# aggregation=NONE is not supported for OnReadVariables.
aggregations = [
    variables_lib.VariableAggregation.SUM,
    variables_lib.VariableAggregation.MEAN,
    variables_lib.VariableAggregation.ONLY_FIRST_REPLICA,
]
options = list(
    x for x in itertools.product(updates, aggregations, [True, False]))
for update, aggregation, cross_replica in options:
    # assign in replica context with SUM does not make sense cause you can
    # just do value * num replicas error is 1. is not a distributed value and
    # is unsupported for aggregation SUM
    if aggregation == variables_lib.VariableAggregation.SUM:
        continue
    with distribution.scope():
        v = variable_scope.variable(
            0.,
            aggregation=aggregation)
    self.evaluate(variables_lib.global_variables_initializer())
    fn, update_value = update
    self.evaluate(assign(fn, v, update_value, cross_replica))
    if cross_replica:
        for component in v._values:
            self.assertAllEqual(expected_cross_replica.get(aggregation),
                                self.evaluate(component.read_value()))
    else:
        for component in v._values:
            self.assertAllEqual(expected_replica.get(aggregation),
                                self.evaluate(component.read_value()))
