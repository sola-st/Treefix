# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.session(graph=ops.Graph()) as sess:
    input_value, inputs, outputs, state_fw, state_bw, sequence_length = (
        self._createBidirectionalRNN(use_shape, True))
    variables_lib.global_variables_initializer().run()
    # Run with pre-specified sequence length of 2, 3
    out, s_fw, s_bw = sess.run(
        [outputs, state_fw, state_bw],
        feed_dict={
            inputs[0]: input_value,
            sequence_length: [2, 3]
        })

    # Since the forward and backward LSTM cells were initialized with the
    # same parameters, the forward and backward output has to be the same,
    # but reversed in time. The format is output[time][batch][depth], and
    # due to depth concatenation (as num_units=3 for both RNNs):
    # - forward output:  out[][][depth] for 0 <= depth < 3
    # - backward output: out[][][depth] for 4 <= depth < 6
    #
    # First sequence in batch is length=2
    # Check that the time=0 forward output is equal to time=1 backward output
    self.assertAllClose(out[0][0][0], out[1][0][3])
    self.assertAllClose(out[0][0][1], out[1][0][4])
    self.assertAllClose(out[0][0][2], out[1][0][5])
    # Check that the time=1 forward output is equal to time=0 backward output
    self.assertAllClose(out[1][0][0], out[0][0][3])
    self.assertAllClose(out[1][0][1], out[0][0][4])
    self.assertAllClose(out[1][0][2], out[0][0][5])

    # Second sequence in batch is length=3
    # Check that the time=0 forward output is equal to time=2 backward output
    self.assertAllClose(out[0][1][0], out[2][1][3])
    self.assertAllClose(out[0][1][1], out[2][1][4])
    self.assertAllClose(out[0][1][2], out[2][1][5])
    # Check that the time=1 forward output is equal to time=1 backward output
    self.assertAllClose(out[1][1][0], out[1][1][3])
    self.assertAllClose(out[1][1][1], out[1][1][4])
    self.assertAllClose(out[1][1][2], out[1][1][5])
    # Check that the time=2 forward output is equal to time=0 backward output
    self.assertAllClose(out[2][1][0], out[0][1][3])
    self.assertAllClose(out[2][1][1], out[0][1][4])
    self.assertAllClose(out[2][1][2], out[0][1][5])
    # Via the reasoning above, the forward and backward final state should be
    # exactly the same
    self.assertAllClose(s_fw, s_bw)
