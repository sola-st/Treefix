# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
input_size = 5
batch_size = 2
state_size = 6
max_length = 8
sequence_length = [4, 6]
with self.session(graph=ops.Graph()) as sess:
    state_saver = TestStateSaver(batch_size, state_size)
    single_input = (array_ops.placeholder(
        dtypes.float32, shape=(None, input_size)),
                    array_ops.placeholder(
                        dtypes.float32, shape=(None, input_size)))
    inputs = max_length * [single_input]
    inputs_c = (array_ops.stack([input_[0] for input_ in inputs]),
                array_ops.stack([input_[1] for input_ in inputs]))
    single_input_using_dim = (array_ops.placeholder(
        dtypes.float32, shape=(batch_size, input_size)),
                              array_ops.placeholder(
                                  dtypes.float32,
                                  shape=(batch_size, input_size)))
    inputs_using_dim = max_length * [single_input_using_dim]

    # Create a cell for the whole test. This is fine because the cell has no
    # variables.
    cell = NestedRNNCell()
    outputs_dynamic, state_dynamic = rnn.dynamic_rnn(
        cell,
        inputs_c,
        dtype=dtypes.float32,
        time_major=True,
        sequence_length=sequence_length)
    outputs_static, state_static = rnn.static_rnn(
        cell, inputs, dtype=dtypes.float32, sequence_length=sequence_length)
    outputs_bid, state_fw, state_bw = rnn.static_bidirectional_rnn(
        cell,
        cell,
        inputs_using_dim,
        dtype=dtypes.float32,
        sequence_length=sequence_length)
    outputs_sav, state_sav = rnn.static_state_saving_rnn(
        cell,
        inputs_using_dim,
        sequence_length=sequence_length,
        state_saver=state_saver,
        state_name=("h", "c"))

    def _assert_same_shape(input1, input2, double=False):
        flat_input1 = nest.flatten(input1)
        flat_input2 = nest.flatten(input2)
        for inp1, inp2 in zip(flat_input1, flat_input2):
            input_shape = inp1.get_shape().as_list()
            if double:
                input_shape[1] *= 2
            self.assertEqual(input_shape, inp2.get_shape().as_list())

    _assert_same_shape(inputs_c, outputs_dynamic)
    _assert_same_shape(inputs, outputs_static)
    _assert_same_shape(inputs_using_dim, outputs_sav)
    _assert_same_shape(inputs_using_dim, outputs_bid, double=True)

    variables_lib.global_variables_initializer().run()

    input_total_size = (batch_size, input_size)
    input_value = (np.random.randn(*input_total_size),
                   np.random.randn(*input_total_size))
    outputs_dynamic_v = sess.run(
        outputs_dynamic, feed_dict={
            single_input: input_value
        })
    outputs_static_v = sess.run(
        outputs_static, feed_dict={
            single_input: input_value
        })
    outputs_sav_v = sess.run(
        outputs_sav, feed_dict={
            single_input_using_dim: input_value
        })
    outputs_bid_v = sess.run(
        outputs_bid, feed_dict={
            single_input_using_dim: input_value
        })

    self.assertAllEqual(outputs_static_v,
                        np.transpose(outputs_dynamic_v, (1, 0, 2, 3)))
    self.assertAllEqual(outputs_static_v, outputs_sav_v)
    outputs_static_array = np.array(outputs_static_v)
    outputs_static_array_double = np.concatenate(
        (outputs_static_array, outputs_static_array), axis=3)
    outputs_bid_array = np.array(outputs_bid_v)
    self.assertAllEqual(outputs_static_array_double, outputs_bid_array)

    state_dynamic_v = sess.run(
        state_dynamic, feed_dict={
            single_input: input_value
        })
    state_static_v = sess.run(
        state_static, feed_dict={
            single_input: input_value
        })
    state_bid_fw_v = sess.run(
        state_fw, feed_dict={
            single_input_using_dim: input_value
        })
    state_bid_bw_v = sess.run(
        state_bw, feed_dict={
            single_input_using_dim: input_value
        })
    state_sav_v = sess.run(
        state_sav, feed_dict={
            single_input_using_dim: input_value
        })
    self.assertAllEqual(np.hstack(state_static_v), np.hstack(state_dynamic_v))
    self.assertAllEqual(np.hstack(state_static_v), np.hstack(state_sav_v))
    self.assertAllEqual(np.hstack(state_static_v), np.hstack(state_bid_fw_v))
    self.assertAllEqual(np.hstack(state_static_v), np.hstack(state_bid_bw_v))
