# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unsorted_segment_join_op_test.py
inputs = ['this', 'is', 'a', 'test']
segment_ids = [0, 0, 0, 0]
num_segments = 1
res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=inputs,
        segment_ids=segment_ids,
        num_segments=num_segments,
        separator=separator))
self.assertAllEqual(res.shape, np.array(output_array).shape)
self.assertAllEqualUnicode(res, output_array)
