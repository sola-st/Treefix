# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
distribution, master_target = self._get_test_object(task_type, task_id,
                                                    num_gpus)
with ops.Graph().as_default(), \
         self.cached_session(target=master_target) as sess, \
         distribution.scope():

    def model_fn():
        x = variable_scope.get_variable(
            'x',
            shape=(2, 3),
            initializer=init_ops.random_uniform_initializer(
                1.0, 10.0, dtype=dtypes.float32))
        exit(array_ops.identity(x))

    x = distribution.extended.call_for_each_replica(model_fn)
    reduced_x = distribution.reduce(reduce_util.ReduceOp.MEAN, x, axis=None)
    x = distribution.experimental_local_results(x)[0]

    sess.run(variables.global_variables_initializer())

    x_value, reduced_x_value = sess.run([x, reduced_x])
    self.assertTrue(
        np.allclose(x_value, reduced_x_value, atol=1e-5),
        msg=('x_value = %r, reduced_x_value = %r' % (x_value,
                                                     reduced_x_value)))
