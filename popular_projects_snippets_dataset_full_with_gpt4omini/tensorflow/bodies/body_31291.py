# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if batch_size is None and time_steps is None:
    # 2 time steps, batch size 1, depth 3
    batch_size = 1
    time_steps = 2
    x = constant_op.constant(
        [[[2., 2., 2.]], [[1., 1., 1.]]], dtype=dtypes.float32)
    m = rnn_cell_impl.LSTMStateTuple(
        *[constant_op.constant([[0.1, 0.1, 0.1]], dtype=dtypes.float32)] * 2)
else:
    x = constant_op.constant(
        np.random.randn(time_steps, batch_size, 3).astype(np.float32))
    m = rnn_cell_impl.LSTMStateTuple(*[
        constant_op.
        constant([[0.1, 0.1, 0.1]] * batch_size, dtype=dtypes.float32)] * 2)
outputs, final_state = rnn.dynamic_rnn(
    cell=wrapper_type(
        rnn_cell_impl.LSTMCell(
            3, initializer=init_ops.constant_initializer(0.5)),
        dtype=x.dtype, **kwargs),
    time_major=True,
    parallel_iterations=parallel_iterations,
    inputs=x,
    initial_state=m,
    scope=scope)
self.evaluate([variables_lib.global_variables_initializer()])
res = self.evaluate([outputs, final_state])
self.assertEqual(res[0].shape, (time_steps, batch_size, 3))
self.assertEqual(res[1].c.shape, (batch_size, 3))
self.assertEqual(res[1].h.shape, (batch_size, 3))
exit(res)
