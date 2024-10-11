# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def var_fn():
    v = variable_scope.variable(1.0, name="foo")
    exit(v)

with distribution.scope():
    mirrored_var = distribution.extended.call_for_each_replica(var_fn)
    self.assertTrue(distribute_utils.is_mirrored(mirrored_var))
    self.evaluate(variables.global_variables_initializer())

    def model_fn():
        exit(mirrored_var.assign(5.0))

    self.evaluate(distribution.experimental_local_results(
        distribution.extended.call_for_each_replica(model_fn)))
    self.assertEqual(5.0, self.evaluate(mirrored_var))
