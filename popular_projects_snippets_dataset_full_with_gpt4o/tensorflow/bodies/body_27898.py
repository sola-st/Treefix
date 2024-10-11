# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
input_lists = _repeat(input_values, 2)

for expected, produced in zip(
    expected_elements, _interleave(input_lists, cycle_length,
                                   block_length)):
    self.assertEqual(expected, produced)
