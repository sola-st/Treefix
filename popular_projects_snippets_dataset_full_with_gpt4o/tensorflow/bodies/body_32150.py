# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unsorted_segment_join_op_test.py
inputs = constant_op.constant([['Y', 'q', 'c'], ['Y', '6', '6'],
                               ['p', 'G', 'a']])
segment_ids = constant_op.constant([1, 0, 1])
num_segments = 2
separator = ':'
output_array = constant_op.constant([['Y', '6', '6'], ['Y:p', 'q:G',
                                                       'c:a']])

res = self.evaluate(
    string_ops.unsorted_segment_join(
        inputs=inputs,
        segment_ids=segment_ids,
        num_segments=num_segments,
        separator=separator))
self.assertAllEqual(res, output_array)
self.assertAllEqual(res.shape, output_array.get_shape())
