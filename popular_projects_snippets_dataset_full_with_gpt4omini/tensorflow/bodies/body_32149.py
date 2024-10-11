# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unsorted_segment_join_op_test.py
inputs = [['Y', 'q', 'c'], ['Y', '6', '6'], ['p', 'G', 'a']]
segment_ids = np.array([1, 0, 1], dtype=np.int32)
num_segments = np.array(2, dtype=np.int32)
separator = ':'
output_array = [['Y', '6', '6'], ['Y:p', 'q:G', 'c:a']]

res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=inputs,
        segment_ids=segment_ids,
        num_segments=num_segments,
        separator=separator))
self.assertAllEqual(res.shape, np.array(output_array).shape)
self.assertAllEqualUnicode(res, output_array)

segment_ids = np.array([1, 0, 1], dtype=np.int64)
num_segments = np.array(2, dtype=np.int64)
res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=inputs,
        segment_ids=segment_ids,
        num_segments=num_segments,
        separator=separator))
self.assertAllEqual(res.shape, np.array(output_array).shape)
self.assertAllEqualUnicode(res, output_array)
