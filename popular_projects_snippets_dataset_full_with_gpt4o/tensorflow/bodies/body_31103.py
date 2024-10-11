# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_decoder_ops_test.py
"""Test one batch, two beams - hibernating beam search."""
# max_time_steps == 8
depth = 6

seq_len_0 = 5
input_prob_matrix_0 = np.asarray(
    [
        [0.30999, 0.309938, 0.0679938, 0.0673362, 0.0708352, 0.173908],
        [0.215136, 0.439699, 0.0370931, 0.0393967, 0.0381581, 0.230517],
        [0.199959, 0.489485, 0.0233221, 0.0251417, 0.0233289, 0.238763],
        [0.279611, 0.452966, 0.0204795, 0.0209126, 0.0194803, 0.20655],
        [0.51286, 0.288951, 0.0243026, 0.0220788, 0.0219297, 0.129878],
        # Random entry added in at time=5
        [0.155251, 0.164444, 0.173517, 0.176138, 0.169979, 0.160671]
    ],
    dtype=np.float32)
# Add arbitrary offset - this is fine
input_prob_matrix_0 = input_prob_matrix_0 + 2.0

# len max_time_steps array of batch_size x depth matrices
inputs = ([
    input_prob_matrix_0[t, :][np.newaxis, :] for t in range(seq_len_0)
]  # Pad to max_time_steps = 8
          + 2 * [np.zeros(
              (1, depth), dtype=np.float32)])

# batch_size length vector of sequence_lengths
seq_lens = np.array([seq_len_0], dtype=np.int32)

# batch_size length vector of log probabilities
log_prob_truth = np.array(
    [
        -5.811451,  # output beam 0
        -6.63339  # output beam 1
    ],
    np.float32)[np.newaxis, :]

# decode_truth: two SparseTensors, (ix, values, shape)
decode_truth = [
    # beam 0, batch 0, two outputs decoded
    (np.array(
        [[0, 0], [0, 1]], dtype=np.int64), np.array(
            [1, 0], dtype=np.int64), np.array(
                [1, 2], dtype=np.int64)),
    # beam 1, batch 0, one output decoded
    (np.array(
        [[0, 0]], dtype=np.int64), np.array(
            [1], dtype=np.int64), np.array(
                [1, 1], dtype=np.int64)),
]

# Test correct decoding.
self._testCTCDecoder(
    ctc_ops.ctc_beam_search_decoder,
    inputs,
    seq_lens,
    log_prob_truth,
    decode_truth,
    beam_width=2,
    top_paths=2)

# Requesting more paths than the beam width allows.
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            (".*requested more paths than the beam "
                             "width.*")):
    self._testCTCDecoder(
        ctc_ops.ctc_beam_search_decoder,
        inputs,
        seq_lens,
        log_prob_truth,
        decode_truth,
        beam_width=2,
        top_paths=3)
