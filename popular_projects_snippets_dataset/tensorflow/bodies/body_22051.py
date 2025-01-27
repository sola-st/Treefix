# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_test.py
with ops.Graph().as_default():
    var0 = variable_scope.get_variable("var0",
                                       initializer=constant_op.constant(1.),
                                       validate_shape=False)

    grads0 = constant_op.constant(0.1, dtype=dtypes.float32)
    learning_rate = lambda: 3.0

    ada_opt = adagrad.AdagradOptimizer(
        learning_rate, initial_accumulator_value=0.1, use_locking=True)

    if not context.executing_eagerly():
        ada_update = ada_opt.apply_gradients(
            zip([grads0], [var0]))
        self.evaluate(variables.global_variables_initializer())

    # Fetch params to validate initial values
    v0_val = self.evaluate([var0])
    self.assertAllClose([1.0], v0_val)

    # Run 3 steps of adagrad
    for _ in range(3):
        if not context.executing_eagerly():
            self.evaluate(ada_update)
        else:
            ada_opt.apply_gradients(zip([grads0], [var0]))

      # Validate updated params
    v0_val = self.evaluate([var0])
    self.assertAllCloseAccordingToType(
        np.array([-1.6026098728179932]), v0_val)
