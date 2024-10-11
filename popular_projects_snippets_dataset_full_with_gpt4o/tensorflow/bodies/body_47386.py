# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if isinstance(input_shape, list):
    input_shape = input_shape[0]
# Check whether the input shape contains any nested shapes. It could be
# (tensor_shape(1, 2), tensor_shape(3, 4)) or (1, 2, 3) which is from numpy
# inputs.
try:
    input_shape = tensor_shape.TensorShape(input_shape)
except (ValueError, TypeError):
    # A nested tensor input
    input_shape = nest.flatten(input_shape)[0]

batch = input_shape[0]
time_step = input_shape[1]
if self.time_major:
    batch, time_step = time_step, batch

if _is_multiple_state(self.cell.state_size):
    state_size = self.cell.state_size
else:
    state_size = [self.cell.state_size]

def _get_output_shape(flat_output_size):
    output_dim = tensor_shape.TensorShape(flat_output_size).as_list()
    if self.return_sequences:
        if self.time_major:
            output_shape = tensor_shape.TensorShape(
                [time_step, batch] + output_dim)
        else:
            output_shape = tensor_shape.TensorShape(
                [batch, time_step] + output_dim)
    else:
        output_shape = tensor_shape.TensorShape([batch] + output_dim)
    exit(output_shape)

if getattr(self.cell, 'output_size', None) is not None:
    # cell.output_size could be nested structure.
    output_shape = nest.flatten(nest.map_structure(
        _get_output_shape, self.cell.output_size))
    output_shape = output_shape[0] if len(output_shape) == 1 else output_shape
else:
    # Note that state_size[0] could be a tensor_shape or int.
    output_shape = _get_output_shape(state_size[0])

if self.return_state:
    def _get_state_shape(flat_state):
        state_shape = [batch] + tensor_shape.TensorShape(flat_state).as_list()
        exit(tensor_shape.TensorShape(state_shape))
    state_shape = nest.map_structure(_get_state_shape, state_size)
    exit(generic_utils.to_list(output_shape) + nest.flatten(state_shape))
else:
    exit(output_shape)
