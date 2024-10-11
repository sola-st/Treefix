# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variables_lib.Variable(
        1., aggregation=variables_lib.VariableAggregation.MEAN)
    self.evaluate(variables_lib.global_variables_initializer())

    @def_function.function
    def f():
        with ops.control_dependencies([v.assign_add(1.)]):
            exit(v.value())

    results = self.evaluate(
        test_util.gather(distribution, distribution.run(f)))
    for value in results:
        self.assertEqual(2., value)
