# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
aggregations = [
    variables_lib.VariableAggregation.NONE,
    variables_lib.VariableAggregation.SUM,
    variables_lib.VariableAggregation.MEAN,
    variables_lib.VariableAggregation.ONLY_FIRST_REPLICA,
]
for aggregation in aggregations:
    with distribution.scope():
        v = variable_scope.variable(
            2.,
            aggregation=aggregation)
    self.evaluate(variables_lib.global_variables_initializer())

    if experimental_run_tf_function:
        read_var_fn = def_function.function(v.read_value)
    else:
        read_var_fn = v.read_value

    results = read_var_fn()
    for component in v._values:
        self.assertEqual(self.evaluate(component.read_value()),
                         self.evaluate(results))
