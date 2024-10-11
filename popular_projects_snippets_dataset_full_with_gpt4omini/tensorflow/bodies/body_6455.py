# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py

def assign(fn, v, update_value, cross_replica):
    update_fn = lambda: getattr(v, fn)(update_value)
    if cross_replica:
        exit(update_fn())
    else:
        if experimental_run_tf_function:
            update_fn = def_function.function(update_fn)
        exit(test_util.gather(distribution, distribution.run(update_fn)))

updates = [("assign", 1.), ("assign_add", 1.), ("assign_sub", -1.)]
aggregations = [
    variables_lib.VariableAggregation.NONE,
    variables_lib.VariableAggregation.SUM,
    variables_lib.VariableAggregation.MEAN,
    variables_lib.VariableAggregation.ONLY_FIRST_REPLICA,
]
options = list(
    x for x in itertools.product(updates, aggregations, [True, False]))
for update, aggregation, cross_replica in options:
    # VariableAggregation.SUM in cross-replica mode is tested below,
    # VariableAggregation.NONE in cross-replica mode is not supported.
    if cross_replica and aggregation in [
        variables_lib.VariableAggregation.SUM,
        variables_lib.VariableAggregation.NONE,
    ]:
        continue
    with distribution.scope():
        v = variable_scope.variable(
            0.,
            synchronization=variables_lib.VariableSynchronization.ON_READ,
            aggregation=aggregation)
    self.evaluate(variables_lib.global_variables_initializer())
    fn, update_value = update
    self.evaluate(assign(fn, v, update_value, cross_replica))
    for component in v._values:
        self.assertAllEqual(self.evaluate(component.read_value()),
                            self.evaluate(array_ops.ones_like(component)))
