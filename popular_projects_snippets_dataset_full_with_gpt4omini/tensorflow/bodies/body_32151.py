# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unsorted_segment_join_op_test.py
inputs = [['Y', 'q', 'c'], ['Y', '6', '6'], ['p', 'G', 'a']]
segment_ids_1 = [1, 0, 1]
num_segments_1 = 2
separator_1 = ':'
output_array_1 = [['Y', '6', '6'], ['Y:p', 'q:G', 'c:a']]

res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=inputs,
        segment_ids=segment_ids_1,
        num_segments=num_segments_1,
        separator=separator_1))
self.assertAllEqualUnicode(res, output_array_1)
self.assertAllEqual(res.shape, np.array(output_array_1).shape)

segment_ids_2 = [1, 1]
num_segments_2 = 2
separator_2 = ''
output_array_2 = [['', '', ''], ['YY:p', '6q:G', '6c:a']]

res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=res,
        segment_ids=segment_ids_2,
        num_segments=num_segments_2,
        separator=separator_2))
self.assertAllEqualUnicode(res, output_array_2)
self.assertAllEqual(res.shape, np.array(output_array_2).shape)
