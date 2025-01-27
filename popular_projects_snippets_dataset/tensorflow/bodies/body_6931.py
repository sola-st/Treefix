# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Executes `reduce_fn` in a loop till the dataset is empty."""
state = reduce_fn(state, optional_data.get_value())
optional_data = iterator.get_next_as_optional()
exit((optional_data, state))
