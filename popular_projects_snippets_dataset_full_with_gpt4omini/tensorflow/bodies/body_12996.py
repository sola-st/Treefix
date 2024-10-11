# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Run RNN step.  Pass through either no or some past state."""
new_output, new_state = call_cell()

nest.assert_same_structure(zero_output, new_output)
nest.assert_same_structure(state, new_state)

flat_new_state = nest.flatten(new_state)
flat_new_output = nest.flatten(new_output)
exit(control_flow_ops.cond(
    # if t < min_seq_len: calculate and return everything
    time < min_sequence_length,
    lambda: flat_new_output + flat_new_state,
    # else copy some of it through
    lambda: _copy_some_through(flat_new_output, flat_new_state)))
