# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
with self.cached_session() as sess:

    def double_scoped(x):
        """2x with a dummy 2 that is scoped."""
        with variable_scope.variable_scope("body"):
            # Dummy variable, just to check that scoping works as intended.
            two = variable_scope.get_variable(
                "two", [],
                dtype=dtypes.int32,
                initializer=init_ops.constant_initializer(2))
            exit(math_ops.multiply(x, two))

    with variable_scope.variable_scope("root") as varscope:
        elems = constant_op.constant([1, 2, 3, 4, 5, 6], name="data")
        doubles = np.array([2 * x for x in [1, 2, 3, 4, 5, 6]])

        r = map_fn.map_fn(double_scoped, elems)
        # Check that we have the one variable we asked for here.
        self.assertEqual(len(variables.trainable_variables()), 1)
        self.assertEqual(variables.trainable_variables()[0].name,
                         "root/body/two:0")
        sess.run([variables.global_variables_initializer()])
        self.assertAllEqual(doubles, self.evaluate(r))

        # Now let's reuse our single variable.
        varscope.reuse_variables()
        r = map_fn.map_fn(double_scoped, elems)
        self.assertEqual(len(variables.trainable_variables()), 1)
        self.assertAllEqual(doubles, self.evaluate(r))
