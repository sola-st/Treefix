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
    # assign in replica context with SUM does not make sense cause you can
    # just do value * num replicas error is 1. is not a distributed value and
    # is unsupported for aggregation SUM
    if (not cross_replica and aggregation ==
        variables_lib.VariableAggregation.SUM):
        continue
    with distribution.scope():
        v = variable_scope.variable(
            0.,
            aggregation=aggregation)
    self.evaluate(variables_lib.global_variables_initializer())
    fn, update_value = update
    self.evaluate(assign(fn, v, update_value, cross_replica))
    for component in v._values:
        self.assertAllEqual(self.evaluate(component.read_value()),
                            self.evaluate(array_ops.ones_like(component)))
