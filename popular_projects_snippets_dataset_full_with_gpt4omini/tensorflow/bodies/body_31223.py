# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
feature_dims = (3, 4, 5)
input_size = feature_dims
batch_size = 2
max_length = 8
sequence_length = [4, 6]
with self.session(graph=ops.Graph()) as sess:
    inputs = max_length * [
        array_ops.placeholder(dtypes.float32, shape=(None,) + input_size)
    ]
    inputs_using_dim = max_length * [
        array_ops.placeholder(
            dtypes.float32, shape=(batch_size,) + input_size)
    ]
    inputs_c = array_ops.stack(inputs)
    # Create a cell for the whole test. This is fine because the cell has no
    # variables.
    cell = DummyMultiDimensionalLSTM(feature_dims)
    state_saver = TestStateSaver(batch_size, input_size)
    outputs_static, state_static = rnn.static_rnn(
        cell, inputs, dtype=dtypes.float32, sequence_length=sequence_length)
    outputs_dynamic, state_dynamic = rnn.dynamic_rnn(
        cell,
        inputs_c,
        dtype=dtypes.float32,
        time_major=True,
        sequence_length=sequence_length)
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

    self.assertEqual(outputs_dynamic.get_shape().as_list(),
                     inputs_c.get_shape().as_list())
    for out, inp in zip(outputs_static, inputs):
        self.assertEqual(out.get_shape().as_list(), inp.get_shape().as_list())
    for out, inp in zip(outputs_bid, inputs_using_dim):
        input_shape_list = inp.get_shape().as_list()
        # fwd and bwd activations are concatenated along the second dim.
        input_shape_list[1] *= 2
        self.assertEqual(out.get_shape().as_list(), input_shape_list)

    variables_lib.global_variables_initializer().run()

    input_total_size = (batch_size,) + input_size
    input_value = np.random.randn(*input_total_size)
    outputs_static_v = sess.run(
        outputs_static, feed_dict={
            inputs[0]: input_value
        })
    outputs_dynamic_v = sess.run(
        outputs_dynamic, feed_dict={
            inputs[0]: input_value
        })
    outputs_bid_v = sess.run(
        outputs_bid, feed_dict={
            inputs_using_dim[0]: input_value
        })
    outputs_sav_v = sess.run(
        outputs_sav, feed_dict={
            inputs_using_dim[0]: input_value
        })

    self.assertAllEqual(outputs_static_v, outputs_dynamic_v)
    self.assertAllEqual(outputs_static_v, outputs_sav_v)
    outputs_static_array = np.array(outputs_static_v)
    outputs_static_array_double = np.concatenate(
        (outputs_static_array, outputs_static_array), axis=2)
    outputs_bid_array = np.array(outputs_bid_v)
    self.assertAllEqual(outputs_static_array_double, outputs_bid_array)

    state_static_v = sess.run(
        state_static, feed_dict={
            inputs[0]: input_value
        })
    state_dynamic_v = sess.run(
        state_dynamic, feed_dict={
            inputs[0]: input_value
        })
    state_bid_fw_v = sess.run(
        state_fw, feed_dict={
            inputs_using_dim[0]: input_value
        })
    state_bid_bw_v = sess.run(
        state_bw, feed_dict={
            inputs_using_dim[0]: input_value
        })
    state_sav_v = sess.run(
        state_sav, feed_dict={
            inputs_using_dim[0]: input_value
        })
    self.assertAllEqual(np.hstack(state_static_v), np.hstack(state_dynamic_v))
    self.assertAllEqual(np.hstack(state_static_v), np.hstack(state_sav_v))
    self.assertAllEqual(np.hstack(state_static_v), np.hstack(state_bid_fw_v))
    self.assertAllEqual(np.hstack(state_static_v), np.hstack(state_bid_bw_v))
