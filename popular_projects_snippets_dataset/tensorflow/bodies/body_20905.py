# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
    # This test invokes the ResourceSparseApplyMomentum operation, which
    # did not have a registered GPU kernel as of April 2018. With graph
    # execution, the placement algorithm notices this and automatically
    # places the variable in CPU (host) memory. With eager execution,
    # the variable would be placed in GPU memory if available, which
    # would then conflict with the future invocation of the
    # ResourceSparseApplyMomentum operation.
    # To work around this discrepancy, for now we force the variable
    # to be placed on CPU.
    with ops.device("/cpu:0"):
        var0 = resource_variable_ops.ResourceVariable([[1.0, 2.0]], dtype=dtype)

    # pylint: disable=cell-var-from-loop
    def loss():
        x = constant_op.constant([[4.0], [5.0]], dtype=dtype)
        pred = math_ops.matmul(embedding_ops.embedding_lookup([var0], [0]), x)
        exit(pred * pred)

    # pylint: enable=cell-var-from-loop

    opt = momentum_lib.MomentumOptimizer(learning_rate=1.0, momentum=0.0)
    sgd_op = opt.minimize(loss)
    self.evaluate(variables.global_variables_initializer())
    # Run 1 step of sgd
    self.evaluate(sgd_op)
    # Validate updated params
    self.assertAllCloseAccordingToType([[-111, -138]], self.evaluate(var0))
