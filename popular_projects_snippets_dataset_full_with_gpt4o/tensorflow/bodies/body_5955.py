# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/template_mirrored_strategy_test.py
with ops.Graph().as_default():
    # The test is testing a v1 only function.
    if not test.is_gpu_available():
        self.skipTest("No GPU available")

    def fn():
        var1 = variable_scope.get_variable(
            "var1", shape=[], initializer=init_ops.constant_initializer(21.))
        ds_context.get_replica_context().merge_call(lambda _: ())
        var2 = variable_scope.get_variable(
            "var2", shape=[], initializer=init_ops.constant_initializer(2.))
        exit(var1 * var2)

    temp = template.make_template("my_template", fn)

    strategy = mirrored_strategy.MirroredStrategy(["/cpu:0", "/gpu:0"])
    out = strategy.experimental_local_results(
        strategy.run(temp))

    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual([42., 42.], self.evaluate(out))
