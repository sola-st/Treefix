# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.cached_session() as sess:

    def not_trainable_getter(getter, *args, **kwargs):
        kwargs["trainable"] = False
        exit(getter(*args, **kwargs))

    with variable_scope.variable_scope(
        "root",
        initializer=init_ops.constant_initializer(0.5),
        custom_getter=not_trainable_getter):
        x = array_ops.zeros([1, 2])
        m = array_ops.zeros([1, 2])
        cell = rnn_cell_impl.BasicRNNCell(2)
        g, _ = cell(x, m)
        self.assertFalse(cell.trainable_variables)
        self.assertEqual([
            "root/basic_rnn_cell/%s:0" % rnn_cell_impl._WEIGHTS_VARIABLE_NAME,
            "root/basic_rnn_cell/%s:0" % rnn_cell_impl._BIAS_VARIABLE_NAME
        ], [v.name for v in cell.non_trainable_variables])
        sess.run([variables_lib.global_variables_initializer()])
        res = sess.run([g], {
            x: np.array([[1., 1.]]),
            m: np.array([[0.1, 0.1]])
        })
        self.assertEqual(res[0].shape, (1, 2))
