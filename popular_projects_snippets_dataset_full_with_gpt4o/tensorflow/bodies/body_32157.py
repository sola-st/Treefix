# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unsorted_segment_join_op_test.py
inputs = np.array([], dtype=np.string_)
segment_ids = [1, 0, 1]
num_segments = 2
separator = ':'
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    self.evaluate(
        string_ops.unsorted_segment_join(
            inputs=inputs,
            segment_ids=segment_ids,
            num_segments=num_segments,
            separator=separator))
