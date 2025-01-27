# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
break_points = self.gen_break_points(self.num_outputs, 10)
expected_outputs = np.repeat(
    np.concatenate([np.arange(10 * x, 11 * x) for x in self.input_values]),
    self.num_repeats).tolist()

actual = self.gen_outputs(
    lambda: self._build_ds(cycle_length, block_length, True),
    break_points, self.num_outputs)
self.assertSequenceEqual(sorted(actual), expected_outputs)
