# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
for index, (expected, produced) in enumerate(
    itertools.zip_longest(
        expected_elements,
        self._interleave(input_lists, cycle_length, block_length))):
    self.assertEqual(expected, produced, "Values differ at %s. %s != %s" %
                     (index, expected, produced))
