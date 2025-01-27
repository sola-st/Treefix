# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
exit((dataset_ops.Dataset.from_tensor_slices(self.input_values).repeat(
    self.num_repeats).apply(
        interleave_ops.parallel_interleave(
            lambda x: dataset_ops.Dataset.range(10 * x, 11 * x),
            cycle_length, block_length, sloppy))))
