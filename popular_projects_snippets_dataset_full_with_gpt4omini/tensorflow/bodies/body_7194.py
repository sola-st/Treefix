# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def var_fn():
    exit(variable_scope.variable(1.0, name="foo"))

with distribution.scope():
    mirrored_var = distribution.extended.call_for_each_replica(var_fn)
    self.assertTrue(distribute_utils.is_mirrored(mirrored_var))
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(1.0, self.evaluate(mirrored_var))
    mirrored_var_result = self.evaluate(mirrored_var.assign(6.0))
    self.assertEqual(6.0, mirrored_var_result)
