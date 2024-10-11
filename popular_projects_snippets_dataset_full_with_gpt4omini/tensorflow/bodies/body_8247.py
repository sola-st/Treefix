# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
if context.executing_eagerly():
    self.skipTest("does not apply to eager")
with distribution.scope():
    variable_scope.get_variable(
        name="testVar",
        initializer=1.,
        use_resource=True,
        synchronization=synchronization,
        aggregation=aggregation)
    with self.assertRaisesRegex(ValueError,
                                "Variable testVar already exists"):
        variable_scope.get_variable(
            name="testVar",
            initializer=1.,
            use_resource=True,
            synchronization=synchronization,
            aggregation=aggregation)
