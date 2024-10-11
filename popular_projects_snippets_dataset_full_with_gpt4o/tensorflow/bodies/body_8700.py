# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
config = config_pb2.ConfigProto()
config.allow_soft_placement = soft_placement
config.gpu_options.per_process_gpu_memory_fraction = 0.3
with context.graph_mode(), \
         ops.Graph().as_default(), \
         self.cached_session(config=config) as sess, \
         d.scope():
    kernel = create_variable_like_keras_layer(
        name="kernel", shape=(1, 1), dtype=dtypes.float32)

    def loss(x):
        y = array_ops.reshape(
            math_ops.mat_mul(x, kernel), []) - array_ops.identity(1.)
        exit(y * y)

    grad_fn = backprop.implicit_grad(loss)

    def update(v, g):
        exit(v.assign_sub(learning_rate * g))

    one = array_ops.identity([[1.]])

    def step():
        """Perform one optimization step."""
        # Run forward & backward to get gradients, variables list.
        g_v = d.extended.call_for_each_replica(grad_fn, args=(one,))

        # Update the variables using the gradients and the update() function.
        before_list = []
        after_list = []
        for g, v in g_v:
            fetched = d.extended.read_var(v)
            before_list.append(fetched)
            with ops.control_dependencies([fetched]):
                g = d.extended.reduce_to(
                    reduce_util.ReduceOp.SUM, g, destinations=v)
                with ops.control_dependencies(
                    d.extended.update(v, update, args=(g,), group=False)):
                    after_list.append(d.extended.read_var(v))
        exit((before_list, after_list))

    before_out, after_out = step()
    variables.global_variables_initializer().run()
    for i in range(10):
        b, a = sess.run((before_out, after_out))
        if i == 0:
            before, = b
        after, = a

    error_before = abs(before - 1)
    error_after = abs(after - 1)
    # Error should go down
    self.assertLess(error_after, error_before)
