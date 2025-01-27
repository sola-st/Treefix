# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
for dtype in [dtypes.float16, dtypes.float32]:
    np_dtype = dtype.as_numpy_dtype
    with self.session(graph=ops.Graph()) as sess:
        with variable_scope.variable_scope(
            "root", initializer=init_ops.constant_initializer(0.5)):
            x = array_ops.zeros([1, 2], dtype=dtype)
            m = array_ops.zeros([1, 8], dtype=dtype)
            cell = rnn_cell_impl.MultiRNNCell(
                [
                    rnn_cell_impl.BasicLSTMCell(2, state_is_tuple=False)
                    for _ in range(2)
                ],
                state_is_tuple=False)
            self.assertEqual(cell.dtype, None)
            self.assertIn("cell-0", cell._trackable_children())
            self.assertIn("cell-1", cell._trackable_children())
            cell.get_config()  # Should not throw an error
            g, out_m = cell(x, m)
            # Layer infers the input type.
            self.assertEqual(cell.dtype, dtype.name)
            expected_variable_names = [
                "root/multi_rnn_cell/cell_0/basic_lstm_cell/%s:0" %
                rnn_cell_impl._WEIGHTS_VARIABLE_NAME,
                "root/multi_rnn_cell/cell_0/basic_lstm_cell/%s:0" %
                rnn_cell_impl._BIAS_VARIABLE_NAME,
                "root/multi_rnn_cell/cell_1/basic_lstm_cell/%s:0" %
                rnn_cell_impl._WEIGHTS_VARIABLE_NAME,
                "root/multi_rnn_cell/cell_1/basic_lstm_cell/%s:0" %
                rnn_cell_impl._BIAS_VARIABLE_NAME
            ]
            self.assertEqual(expected_variable_names,
                             [v.name for v in cell.trainable_variables])
            self.assertFalse(cell.non_trainable_variables)
            sess.run([variables_lib.global_variables_initializer()])
            res = sess.run([g, out_m], {
                x: np.array([[1., 1.]]),
                m: 0.1 * np.ones([1, 8])
            })
            self.assertEqual(len(res), 2)
            variables = variables_lib.global_variables()
            self.assertEqual(expected_variable_names, [v.name for v in variables])
            # The numbers in results were not calculated, this is just a
            # smoke test.
            self.assertAllClose(res[0], np.array(
                [[0.240, 0.240]], dtype=np_dtype), 1e-2)
            expected_mem = np.array(
                [[0.689, 0.689, 0.448, 0.448, 0.398, 0.398, 0.240, 0.240]],
                dtype=np_dtype)
            self.assertAllClose(res[1], expected_mem, 1e-2)
        with variable_scope.variable_scope(
            "other", initializer=init_ops.constant_initializer(0.5)):
            # Test BasicLSTMCell with input_size != num_units.
            x = array_ops.zeros([1, 3], dtype=dtype)
            m = array_ops.zeros([1, 4], dtype=dtype)
            g, out_m = rnn_cell_impl.BasicLSTMCell(2, state_is_tuple=False)(x, m)
            sess.run([variables_lib.global_variables_initializer()])
            res = sess.run(
                [g, out_m], {
                    x: np.array([[1., 1., 1.]], dtype=np_dtype),
                    m: 0.1 * np.ones([1, 4], dtype=np_dtype)
                })
            self.assertEqual(len(res), 2)
