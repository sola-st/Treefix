# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
# Non-empty input leading to empty output.
self._clear_coordination_events()
next_element = self.getNext(
    self.dataset_fn(
        input_values=np.int64([0, 0, 0]),
        cycle_length=2,
        block_length=3,
        sloppy=sloppy,
        buffer_output_elements=1,
        prefetch_input_elements=0))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
