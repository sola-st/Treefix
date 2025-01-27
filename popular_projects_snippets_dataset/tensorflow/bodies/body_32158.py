# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unsorted_segment_join_op_test.py
inputs = [['Y', 'q', 'c'], ['Y', '6', '6'], ['p', 'G', 'a']]
segment_ids = [-1, 0, -1]
num_segments = 1
separator = ':'
with self.assertRaises(errors_impl.InvalidArgumentError):
    self.evaluate(
        string_ops.unsorted_segment_join(
            inputs=inputs,
            segment_ids=segment_ids,
            num_segments=num_segments,
            separator=separator))
