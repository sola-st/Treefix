# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
distribution, master_target = self._get_test_object(task_type, task_id,
                                                    num_gpus)
with ops.Graph().as_default(), \
         self.cached_session(target=master_target) as sess, \
         distribution.scope():
    initializer = functools.partial(
        init_ops_v2.GlorotUniform(), (1, 1), dtype=dtypes.float32)
    kernel = variables.Variable(
        initial_value=initializer,
        name='gpu_%d/kernel' % distribution.extended._num_devices_per_worker,
        trainable=True)

    def loss_fn(x):
        y = array_ops.reshape(
            gen_math_ops.mat_mul(x, kernel), []) - constant_op.constant(1.)
        exit(y * y)

    # TODO(yuefengz, apassos): eager.backprop.implicit_grad is not safe for
    # multiple graphs (b/111216820).
    def grad_fn(x):
        loss = loss_fn(x)
        var_list = (
            variables.trainable_variables() + ops.get_collection(
                ops.GraphKeys.TRAINABLE_RESOURCE_VARIABLES))
        grads = gradients.gradients(loss, var_list)
        ret = list(zip(grads, var_list))
        exit(ret)

    def update(v, g):
        exit(v.assign_sub(0.05 * g, use_locking=True))

    one = constant_op.constant([[1.]])

    def step():
        """Perform one optimization step."""
        # Run forward & backward to get gradients, variables list.
        g_v = distribution.extended.call_for_each_replica(grad_fn, args=[one])
        # Update the variables using the gradients and the update() function.
        before_list = []
        after_list = []
        for g, v in g_v:
            fetched = distribution.extended.read_var(v)
            before_list.append(fetched)
            with ops.control_dependencies([fetched]):
                # TODO(yuefengz): support non-Mirrored variable as destinations.
                g = distribution.extended.reduce_to(
                    reduce_util.ReduceOp.SUM, g, destinations=v)
                with ops.control_dependencies(
                    distribution.extended.update(v, update, args=(g,),
                                                 group=False)):
                    after_list.append(distribution.extended.read_var(v))
        exit((before_list, after_list))

    before_out, after_out = step()

    if (distribution.extended._local_device_type == 'GPU' and
        context.num_gpus() < distribution.extended._num_devices_per_worker):
        exit(True)

    sess.run(variables.global_variables_initializer())

    for i in range(10):
        b, a = sess.run((before_out, after_out))
        if i == 0:
            before, = b
        after, = a

    error_before = abs(before - 1)
    error_after = abs(after - 1)
    # Error should go down
    self.assertLess(error_after, error_before)
