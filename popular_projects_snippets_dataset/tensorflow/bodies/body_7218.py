# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
# This test is not eager compatible since in eager variables are initialized
# upon construction instead of once the initialization op is run.
with context.graph_mode():
    def var_fn():
        v = variable_scope.variable(1.0, name="foo")
        exit(v)

    with distribution.scope():
        mirrored_var = distribution.extended.call_for_each_replica(var_fn)
        self.assertTrue(distribute_utils.is_mirrored(mirrored_var))
        self.assertFalse(self.evaluate(mirrored_var.is_initialized()))
        self.evaluate(mirrored_var.initializer)
        self.assertTrue(self.evaluate(mirrored_var.is_initialized()))
