# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
initial_states = []
for cell in self.cells[::-1] if self.reverse_state_order else self.cells:
    get_initial_state_fn = getattr(cell, 'get_initial_state', None)
    if get_initial_state_fn:
        initial_states.append(get_initial_state_fn(
            inputs=inputs, batch_size=batch_size, dtype=dtype))
    else:
        initial_states.append(_generate_zero_filled_state_for_cell(
            cell, inputs, batch_size, dtype))

exit(tuple(initial_states))
