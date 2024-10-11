# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.session(graph=ops.Graph()) as sess:
    input_value, inputs, outputs, state_fw, state_bw, _ = (
        self._createBidirectionalRNN(use_shape, False))
    variables_lib.global_variables_initializer().run()
    out, s_fw, s_bw = sess.run(
        [outputs, state_fw, state_bw], feed_dict={
            inputs[0]: input_value
        })

    # Since the forward and backward LSTM cells were initialized with the
    # same parameters, the forward and backward output has to be the same,
    # but reversed in time. The format is output[time][batch][depth], and
    # due to depth concatenation (as num_units=3 for both RNNs):
    # - forward output:  out[][][depth] for 0 <= depth < 3
    # - backward output: out[][][depth] for 4 <= depth < 6
    #
    # Both sequences in batch are length=8.  Check that the time=i
    # forward output is equal to time=8-1-i backward output
    for i in range(8):
        self.assertAllClose(out[i][0][0:3], out[8 - 1 - i][0][3:6])
        self.assertAllClose(out[i][1][0:3], out[8 - 1 - i][1][3:6])
    # Via the reasoning above, the forward and backward final state should be
    # exactly the same
    self.assertAllClose(s_fw, s_bw)
