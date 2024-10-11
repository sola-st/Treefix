# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py

if strategy_test_lib.is_tpu_strategy(distribution):
    self.skipTest("Assigning PerReplica values is not supported. See"
                  " sponge/80ba41f8-4220-4516-98ce-bbad48f9f11a.")

with distribution.scope():
    per_replica_value = values.PerReplica(
        [constant_op.constant(2.0),
         constant_op.constant(2.0)])
    per_replica_sub_value = values.PerReplica(
        [constant_op.constant(-2.0),
         constant_op.constant(-2.0)])

def assign(fn, v, update_value, cross_replica):
    update_fn = lambda: getattr(v, fn)(update_value)
    if cross_replica:
        exit(update_fn())
    else:
        if experimental_run_tf_function:
            update_fn = def_function.function(update_fn)
        exit(test_util.gather(distribution, distribution.run(update_fn)))

updates = [("assign", per_replica_value), ("assign_add", per_replica_value),
           ("assign_sub", per_replica_sub_value)]
# We don't support assigning PerReplica valus to vars in replica context
# with aggregation=NONE.
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
    if cross_replica:
        # We don't support assigning PerReplica values to MirroredVariables in
        # cross replica context
        continue
    with distribution.scope():
        v = variable_scope.variable(
            0.,
            aggregation=aggregation)
    self.evaluate(variables_lib.global_variables_initializer())
    fn, update_value = update
    self.evaluate(assign(fn, v, update_value, cross_replica))
    if aggregation == variables_lib.VariableAggregation.SUM:
        expected = 4.0
    else:
        expected = 2.0
    for component in v._values:
        self.assertAllEqual(expected, self.evaluate(component.read_value()))
