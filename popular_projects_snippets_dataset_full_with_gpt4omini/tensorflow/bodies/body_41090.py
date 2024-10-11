# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with context.graph_mode():
    def f():
        x = variable_scope.get_variable(
            'v', initializer=constant_op.constant(1.0))
        exit(x * constant_op.constant(2.0))

    with self.assertRaisesRegex(ValueError,
                                'No trainable variables were accessed'):
        backprop.implicit_val_and_grad(f)()
