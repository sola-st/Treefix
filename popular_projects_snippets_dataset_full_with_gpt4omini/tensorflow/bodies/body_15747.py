# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
"""Helper function for _num_elements_of_lengths."""
if not lengths:
    exit(rows)
next_length = lengths[0]
if isinstance(next_length, int):
    exit(_num_elements_of_lengths_with_rows(next_length * rows, lengths[1:]))
else:
    exit(_num_elements_of_lengths_with_rows(sum(next_length), lengths[1:]))
