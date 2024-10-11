# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_test.py
for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
    if use_resource:
        var0 = resource_variable_ops.ResourceVariable([1.0, 2.0], dtype=dtype)
        var1 = resource_variable_ops.ResourceVariable([3.0, 4.0], dtype=dtype)
    else:
        var0 = variables.Variable([1.0, 2.0], dtype=dtype)
        var1 = variables.Variable([3.0, 4.0], dtype=dtype)
    grads0 = constant_op.constant([0.1, 0.1], dtype=dtype)
    grads1 = constant_op.constant([0.01, 0.01], dtype=dtype)

    learning_rate = lambda: 3.0
    if not use_callable_params:
        learning_rate = learning_rate()

    ada_opt = adagrad.AdagradOptimizer(
        learning_rate, initial_accumulator_value=0.1, use_locking=use_locking)

    if not context.executing_eagerly():
        ada_update = ada_opt.apply_gradients(
            zip([grads0, grads1], [var0, var1]))
        self.evaluate(variables.global_variables_initializer())

    # Fetch params to validate initial values
    v0_val, v1_val = self.evaluate([var0, var1])
    self.assertAllClose([1.0, 2.0], v0_val)
    self.assertAllClose([3.0, 4.0], v1_val)

    # Run 3 steps of adagrad
    for _ in range(3):
        if not context.executing_eagerly():
            self.evaluate(ada_update)
        else:
            ada_opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

      # Validate updated params
    v0_val, v1_val = self.evaluate([var0, var1])
    self.assertAllCloseAccordingToType(
        np.array([-1.6026098728179932, -0.6026098728179932]), v0_val)
    self.assertAllCloseAccordingToType(
        np.array([2.715679168701172, 3.715679168701172]), v1_val)
