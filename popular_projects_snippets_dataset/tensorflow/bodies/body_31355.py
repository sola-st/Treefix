# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
with self.session(graph=ops_lib.Graph()) as sess:
    basic_cell = rnn_cell_impl.BasicLSTMCell(1)
    basic_cell(array_ops.ones([1, 1]),
               state=basic_cell.get_initial_state(inputs=None,
                                                  batch_size=1,
                                                  dtype=dtypes.float32))
    self.evaluate([v.initializer for v in basic_cell.variables])
    self.evaluate(basic_cell._bias.assign([10.] * 4))
    save = saver.Saver()
    prefix = os.path.join(self.get_temp_dir(), "ckpt")
    save_path = save.save(sess, prefix)

with self.session(graph=ops_lib.Graph()) as sess:
    lstm_cell = rnn_cell_impl.LSTMCell(1, name="basic_lstm_cell")
    lstm_cell(array_ops.ones([1, 1]),
              state=lstm_cell.get_initial_state(inputs=None,
                                                batch_size=1,
                                                dtype=dtypes.float32))
    self.evaluate([v.initializer for v in lstm_cell.variables])
    save = saver.Saver()
    save.restore(sess, save_path)
    self.assertAllEqual([10.] * 4, self.evaluate(lstm_cell._bias))
