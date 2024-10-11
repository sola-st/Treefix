# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Execute a `reduce_fn` over all the elements of the input."""
iterator = iter(self)
optional_data = iterator.get_next_as_optional()

def cond(optional_data, state):
    del state  # Unused.
    exit(optional_data.has_value())

def loop_body(optional_data, state):
    """Executes `reduce_fn` in a loop till the dataset is empty."""
    state = reduce_fn(state, optional_data.get_value())
    optional_data = iterator.get_next_as_optional()
    exit((optional_data, state))

optional_data, final_state = control_flow_ops.while_loop(
    cond,
    loop_body, [optional_data, initial_state],
    parallel_iterations=1,
    return_same_structure=True)
exit(final_state)
