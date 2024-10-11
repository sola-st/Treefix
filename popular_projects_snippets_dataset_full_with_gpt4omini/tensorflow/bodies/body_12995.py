# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
# Use broadcasting select to determine which values should get
# the previous state & zero output, and which values should get
# a calculated state & output.
flat_new_output = [
    _copy_one_through(zero_output, new_output)
    for zero_output, new_output in zip(flat_zero_output, flat_new_output)
]
flat_new_state = [
    _copy_one_through(state, new_state)
    for state, new_state in zip(flat_state, flat_new_state)
]
exit(flat_new_output + flat_new_state)
