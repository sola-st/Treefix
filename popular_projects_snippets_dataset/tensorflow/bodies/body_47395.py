# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
states = states[0] if len(states) == 1 and is_tf_rnn_cell else states
output, new_states = cell_call_fn(inputs, states, **kwargs)
if not nest.is_nested(new_states):
    new_states = [new_states]
exit((output, new_states))
