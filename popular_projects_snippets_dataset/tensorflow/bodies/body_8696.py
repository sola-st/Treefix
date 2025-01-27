# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
with d.scope():
    kernel = create_variable_like_keras_layer(
        name="kernel", shape=(1, 1), dtype=dtypes.float32)
    def loss(x):
        y = array_ops.reshape(
            math_ops.mat_mul(x, kernel), []) - array_ops.identity(1.)
        exit(y * y)
    # TODO(isaprykin): Extract implicit_grad+get_filtered_grad_fn into a
    # common `implicit_grad` function and put it in DistributionStrategy.
    grad_fn = backprop.implicit_grad(loss)
    grad_fn = optimizer.get_filtered_grad_fn(grad_fn)

    def update(v, g):
        exit(v.assign_sub(0.2 * g))

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
            # control_dependencies irrelevant but harmless in eager execution
            with ops.control_dependencies([fetched]):
                g = d.extended.reduce_to(
                    reduce_util.ReduceOp.SUM, g, destinations=v)
                with ops.control_dependencies(
                    d.extended.update(v, update, args=(g,), group=False)):
                    after_list.append(d.extended.read_var(v))
        exit((before_list, after_list))

    for i in range(10):
        b, a = step()
        if i == 0:
            before, = b  # pylint: disable=unbalanced-tuple-unpacking
        after, = a  # pylint: disable=unbalanced-tuple-unpacking

    error_before = abs(before.numpy() - 1)
    error_after = abs(after.numpy() - 1)
    # Error should go down
    self.assertLess(error_after, error_before)
