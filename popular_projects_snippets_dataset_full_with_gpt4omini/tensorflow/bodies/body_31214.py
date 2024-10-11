# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.session(graph=ops.Graph()) as sess:
    input_value, inputs, outputs, state_fw, state_bw, sequence_length = (
        self._createBidirectionalDynamicRNN(
            use_shape, use_state_tuple, use_time_major, use_sequence_length))
    variables_lib.global_variables_initializer().run()
    # Run with pre-specified sequence length of 2, 3
    feed_dict = ({sequence_length: [2, 3]} if use_sequence_length else {})
    feed_dict.update({inputs[0]: input_value})
    if use_state_tuple:
        out, c_fw, m_fw, c_bw, m_bw = sess.run(
            [outputs, state_fw[0], state_fw[1], state_bw[0], state_bw[1]],
            feed_dict=feed_dict)
        s_fw = (c_fw, m_fw)
        s_bw = (c_bw, m_bw)
    else:
        feed_dict.update({inputs[0]: input_value})
        out, s_fw, s_bw = sess.run(
            [outputs, state_fw, state_bw], feed_dict=feed_dict)

    # Since the forward and backward LSTM cells were initialized with the
    # same parameters, the forward and backward output has to be the same,
    # but reversed in time. The format is output[time][batch][depth], and
    # due to depth concatenation (as num_units=3 for both RNNs):
    # - forward output:  out[][][depth] for 0 <= depth < 3
    # - backward output: out[][][depth] for 4 <= depth < 6
    #
    if not use_time_major:
        out = np.swapaxes(out, 0, 1)

    if use_sequence_length:
        # First sequence in batch is length=2
        # Check that the t=0 forward output is equal to t=1 backward output
        self.assertEqual(out[0][0][0], out[1][0][3])
        self.assertEqual(out[0][0][1], out[1][0][4])
        self.assertEqual(out[0][0][2], out[1][0][5])
        # Check that the t=1 forward output is equal to t=0 backward output
        self.assertEqual(out[1][0][0], out[0][0][3])
        self.assertEqual(out[1][0][1], out[0][0][4])
        self.assertEqual(out[1][0][2], out[0][0][5])

        # Second sequence in batch is length=3
        # Check that the t=0 forward output is equal to t=2 backward output
        self.assertEqual(out[0][1][0], out[2][1][3])
        self.assertEqual(out[0][1][1], out[2][1][4])
        self.assertEqual(out[0][1][2], out[2][1][5])
        # Check that the t=1 forward output is equal to t=1 backward output
        self.assertEqual(out[1][1][0], out[1][1][3])
        self.assertEqual(out[1][1][1], out[1][1][4])
        self.assertEqual(out[1][1][2], out[1][1][5])
        # Check that the t=2 forward output is equal to t=0 backward output
        self.assertEqual(out[2][1][0], out[0][1][3])
        self.assertEqual(out[2][1][1], out[0][1][4])
        self.assertEqual(out[2][1][2], out[0][1][5])
        # Via the reasoning above, the forward and backward final state should
        # be exactly the same
        self.assertAllClose(s_fw, s_bw)
    else:  # not use_sequence_length
        max_length = 8  # from createBidirectionalDynamicRNN
        for t in range(max_length):
            self.assertAllEqual(out[t, :, 0:3], out[max_length - t - 1, :, 3:6])
        self.assertAllClose(s_fw, s_bw)
