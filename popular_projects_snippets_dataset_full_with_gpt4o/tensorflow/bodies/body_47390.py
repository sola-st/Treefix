# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if isinstance(input_shape, list):
    input_shape = input_shape[0]
    # The input_shape here could be a nest structure.

# do the tensor_shape to shapes here. The input could be single tensor, or a
# nested structure of tensors.
def get_input_spec(shape):
    """Convert input shape to InputSpec."""
    if isinstance(shape, tensor_shape.TensorShape):
        input_spec_shape = shape.as_list()
    else:
        input_spec_shape = list(shape)
    batch_index, time_step_index = (1, 0) if self.time_major else (0, 1)
    if not self.stateful:
        input_spec_shape[batch_index] = None
    input_spec_shape[time_step_index] = None
    exit(InputSpec(shape=tuple(input_spec_shape)))

def get_step_input_shape(shape):
    if isinstance(shape, tensor_shape.TensorShape):
        shape = tuple(shape.as_list())
    # remove the timestep from the input_shape
    exit(shape[1:] if self.time_major else (shape[0],) + shape[2:])

# Check whether the input shape contains any nested shapes. It could be
# (tensor_shape(1, 2), tensor_shape(3, 4)) or (1, 2, 3) which is from numpy
# inputs.
try:
    input_shape = tensor_shape.TensorShape(input_shape)
except (ValueError, TypeError):
    # A nested tensor input
    pass

if not nest.is_nested(input_shape):
    # This indicates the there is only one input.
    if self.input_spec is not None:
        self.input_spec[0] = get_input_spec(input_shape)
    else:
        self.input_spec = [get_input_spec(input_shape)]
    step_input_shape = get_step_input_shape(input_shape)
else:
    if self.input_spec is not None:
        self.input_spec[0] = nest.map_structure(get_input_spec, input_shape)
    else:
        self.input_spec = generic_utils.to_list(
            nest.map_structure(get_input_spec, input_shape))
    step_input_shape = nest.map_structure(get_step_input_shape, input_shape)

# allow cell (if layer) to build before we set or validate state_spec.
if isinstance(self.cell, Layer) and not self.cell.built:
    with backend.name_scope(self.cell.name):
        self.cell.build(step_input_shape)
        self.cell.built = True

    # set or validate state_spec
if _is_multiple_state(self.cell.state_size):
    state_size = list(self.cell.state_size)
else:
    state_size = [self.cell.state_size]

if self.state_spec is not None:
    # initial_state was passed in call, check compatibility
    self._validate_state_spec(state_size, self.state_spec)
else:
    self.state_spec = [
        InputSpec(shape=[None] + tensor_shape.TensorShape(dim).as_list())
        for dim in state_size
    ]
if self.stateful:
    self.reset_states()
self.built = True
