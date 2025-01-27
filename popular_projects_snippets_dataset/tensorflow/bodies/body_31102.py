# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_decoder_ops_test.py
"""Test two batch entries - best path decoder."""
max_time_steps = 6
# depth == 4
seq_len_0 = 4
input_prob_matrix_0 = np.asarray(
    [
        [1.0, 0.0, 0.0, 0.0],  # t=0
        [0.0, 0.0, 0.4, 0.6],  # t=1
        [0.0, 0.0, 0.4, 0.6],  # t=2
        [0.0, 0.9, 0.1, 0.0],  # t=3
        [0.0, 0.0, 0.0, 0.0],  # t=4 (ignored)
        [0.0, 0.0, 0.0, 0.0]
    ],  # t=5 (ignored)
    dtype=np.float32)
input_log_prob_matrix_0 = np.log(input_prob_matrix_0)

seq_len_1 = 5
# dimensions are time x depth
input_prob_matrix_1 = np.asarray(
    [
        [0.1, 0.9, 0.0, 0.0],  # t=0
        [0.0, 0.9, 0.1, 0.0],  # t=1
        [0.0, 0.0, 0.1, 0.9],  # t=2
        [0.0, 0.9, 0.1, 0.1],  # t=3
        [0.9, 0.1, 0.0, 0.0],  # t=4
        [0.0, 0.0, 0.0, 0.0]  # t=5 (ignored)
    ],
    dtype=np.float32)
input_log_prob_matrix_1 = np.log(input_prob_matrix_1)

# len max_time_steps array of batch_size x depth matrices
inputs = np.array([
    np.vstack(
        [input_log_prob_matrix_0[t, :], input_log_prob_matrix_1[t, :]])
    for t in range(max_time_steps)
])

# batch_size length vector of sequence_lengths
seq_lens = np.array([seq_len_0, seq_len_1], dtype=np.int32)

# batch_size length vector of negative log probabilities
log_prob_truth = np.array([
    np.sum(-np.log([1.0, 0.6, 0.6, 0.9])),
    np.sum(-np.log([0.9, 0.9, 0.9, 0.9, 0.9]))
], np.float32)[:, np.newaxis]

# decode_truth: one SparseTensor (ix, vals, shape)
decode_truth = [
    (
        np.array(
            [
                [0, 0],  # batch 0, 2 outputs
                [0, 1],
                [1, 0],  # batch 1, 3 outputs
                [1, 1],
                [1, 2]
            ],
            dtype=np.int64),
        np.array(
            [
                0,  # batch 0, 2 values
                1,
                1,  # batch 1, 3 values
                1,
                0
            ],
            dtype=np.int64),
        # shape is batch x max_decoded_length
        np.array([2, 3], dtype=np.int64)),
]

# Test without defining blank_index
self._testCTCDecoder(ctc_ops.ctc_greedy_decoder, inputs, seq_lens,
                     log_prob_truth, decode_truth)

# Shift blank_index to be somewhere in the middle of inputs
blank_index = 2
inputs = np.concatenate(
    (inputs[:, :, :blank_index], inputs[:, :, -1:], inputs[:, :,
                                                           blank_index:-1]),
    axis=2)

# Test positive value in blank_index
self._testCTCDecoder(
    ctc_ops.ctc_greedy_decoder,
    inputs,
    seq_lens,
    log_prob_truth,
    decode_truth,
    blank_index=2)

# Test negative value in blank_index
self._testCTCDecoder(
    ctc_ops.ctc_greedy_decoder,
    inputs,
    seq_lens,
    log_prob_truth,
    decode_truth,
    blank_index=-2)
