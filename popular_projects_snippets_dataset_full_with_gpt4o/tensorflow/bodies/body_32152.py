# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unsorted_segment_join_op_test.py
res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=inputs,
        segment_ids=segment_ids,
        num_segments=num_segments,
        separator=separator))
self.assertAllEqualUnicode(res, output_array)
self.assertAllEqual(res.shape, np.array(output_array).shape)
