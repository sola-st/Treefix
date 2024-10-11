# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_decoder_ops_test.py
inputs_t = [ops.convert_to_tensor(x) for x in inputs]
# convert inputs_t into a [max_time x batch_size x depth] tensor
# from a len time python list of [batch_size x depth] tensors
inputs_t = array_ops.stack(inputs_t)

with self.cached_session(use_gpu=False) as sess:
    decoded_list, log_probability = decoder(
        inputs_t, sequence_length=seq_lens, **decoder_args)
    decoded_unwrapped = list(
        flatten([(st.indices, st.values, st.dense_shape) for st in
                 decoded_list]))

    if expected_err_re is None:
        outputs = sess.run(decoded_unwrapped + [log_probability])

        # Group outputs into (ix, vals, shape) tuples
        output_sparse_tensors = list(grouper(outputs[:-1], 3))

        output_log_probability = outputs[-1]

        # Check the number of decoded outputs (top_paths) match
        self.assertEqual(len(output_sparse_tensors), len(decode_truth))

        # For each SparseTensor tuple, compare (ix, vals, shape)
        for out_st, truth_st, tf_st in zip(output_sparse_tensors, decode_truth,
                                           decoded_list):
            self.assertAllEqual(out_st[0], truth_st[0])  # ix
            self.assertAllEqual(out_st[1], truth_st[1])  # vals
            self.assertAllEqual(out_st[2], truth_st[2])  # shape
            # Compare the shapes of the components with the truth. The
            # `None` elements are not known statically.
            self.assertEqual([None, truth_st[0].shape[1]],
                             tf_st.indices.get_shape().as_list())
            self.assertEqual([None], tf_st.values.get_shape().as_list())
            self.assertShapeEqual(truth_st[2], tf_st.dense_shape)

        # Make sure decoded probabilities match
        self.assertAllClose(output_log_probability, log_prob_truth, atol=1e-6)
    else:
        with self.assertRaisesOpError(expected_err_re):
            sess.run(decoded_unwrapped + [log_probability])
