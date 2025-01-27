# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Validate the state spec between the initial_state and the state_size.

    Args:
      cell_state_sizes: list, the `state_size` attribute from the cell.
      init_state_specs: list, the `state_spec` from the initial_state that is
        passed in `call()`.

    Raises:
      ValueError: When initial state spec is not compatible with the state size.
    """
validation_error = ValueError(
    'An `initial_state` was passed that is not compatible with '
    '`cell.state_size`. Received `state_spec`={}; '
    'however `cell.state_size` is '
    '{}'.format(init_state_specs, cell_state_sizes))
flat_cell_state_sizes = nest.flatten(cell_state_sizes)
flat_state_specs = nest.flatten(init_state_specs)

if len(flat_cell_state_sizes) != len(flat_state_specs):
    raise validation_error
for cell_state_spec, cell_state_size in zip(flat_state_specs,
                                            flat_cell_state_sizes):
    if not tensor_shape.TensorShape(
        # Ignore the first axis for init_state which is for batch
        cell_state_spec.shape[1:]).is_compatible_with(
            tensor_shape.TensorShape(cell_state_size)):
        raise validation_error
