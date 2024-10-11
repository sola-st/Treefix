# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
exit(dataset_ops.Dataset.from_tensor_slices(input_values).map(
    map_fn).repeat(self.repeat_count).apply(
        interleave_ops.parallel_interleave(
            interleave_fn, cycle_length, block_length, sloppy,
            buffer_output_elements, prefetch_input_elements)))
