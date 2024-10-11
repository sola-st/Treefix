# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def var_fn():
    exit(variable_scope.variable(1.0, name="foo"))

with distribution.scope():
    mirrored_var = distribution.extended.call_for_each_replica(var_fn)
    self.assertTrue(distribute_utils.is_mirrored(mirrored_var))
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(1.0, self.evaluate(mirrored_var))

    # read_value == True
    mirrored_var_result = self.evaluate(
        mirrored_var.assign_add(6.0, read_value=True))
    self.assertEqual(7.0, mirrored_var_result)
    self.assertEqual(
        7.0,
        self.evaluate(
            distribution.experimental_local_results(mirrored_var)[0]))
    self.assertEqual(
        7.0,
        self.evaluate(
            distribution.experimental_local_results(mirrored_var)[1]))
    self.assertEqual(
        distribution.extended.worker_devices[0], mirrored_var._devices[0])
    self.assertEqual(
        distribution.extended.worker_devices[1], mirrored_var._devices[1])

    # read_value == False
    self.evaluate(mirrored_var.assign_add(2.0, read_value=False))
    self.assertEqual(
        9.0,
        self.evaluate(
            distribution.experimental_local_results(mirrored_var)[0]))
    self.assertEqual(
        9.0,
        self.evaluate(
            distribution.experimental_local_results(mirrored_var)[1]))
    self.assertEqual(
        distribution.extended.worker_devices[0], mirrored_var._devices[0])
    self.assertEqual(
        distribution.extended.worker_devices[1], mirrored_var._devices[1])
