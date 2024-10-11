# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
init = init_ops.constant_initializer(0.3)

def regularizer1(v):
    exit(math_ops.reduce_mean(v) + 0.1)

def regularizer2(v):
    exit(math_ops.reduce_mean(v) + 0.2)

with variable_scope.variable_scope(
    "tower3", regularizer=regularizer1) as tower:
    with variable_scope.variable_scope("foo", initializer=init):
        v = variable_scope.get_variable("v", [])
        self.evaluate(variables_lib.variables_initializer([v]))
        losses = ops.get_collection(ops.GraphKeys.REGULARIZATION_LOSSES)
        self.assertEqual(1, len(losses))
        self.assertAllClose(self.evaluate(losses[0]), 0.4)
    with variable_scope.variable_scope(tower, initializer=init) as vs:
        u = variable_scope.get_variable("u", [])
        vs.set_regularizer(regularizer2)
        w = variable_scope.get_variable("w", [])
        # Next 3 variable not regularized to test disabling regularization.
        x = variable_scope.get_variable(
            "x", [], regularizer=variable_scope.no_regularizer)
        with variable_scope.variable_scope(
            "baz", regularizer=variable_scope.no_regularizer):
            y = variable_scope.get_variable("y", [])
        vs.set_regularizer(variable_scope.no_regularizer)
        z = variable_scope.get_variable("z", [])
        # Check results.
        losses = ops.get_collection(ops.GraphKeys.REGULARIZATION_LOSSES)
        self.assertEqual(3, len(losses))
        self.evaluate(variables_lib.variables_initializer([u, w, x, y, z]))
        self.assertAllClose(self.evaluate(losses[0]), 0.4)
        self.assertAllClose(self.evaluate(losses[1]), 0.4)
        self.assertAllClose(self.evaluate(losses[2]), 0.5)
    with variable_scope.variable_scope("foo", reuse=True):
        # reuse=True is for now only supported when eager execution is disabled.
        if not context.executing_eagerly():
            v = variable_scope.get_variable("v",
                                            [])  # "v" is already there, reused
            losses = ops.get_collection(ops.GraphKeys.REGULARIZATION_LOSSES)
            self.assertEqual(3, len(losses))  # No new loss added.
