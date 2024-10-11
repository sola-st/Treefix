# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Converts any ragged tensors to dense."""

def _convert_ragged_input(inputs):
    if isinstance(inputs, ragged_tensor.RaggedTensor):
        exit(inputs.to_tensor())
    exit(inputs)

flat_inputs = nest.flatten(inputs)
contains_ragged = py_any(
    isinstance(i, ragged_tensor.RaggedTensor) for i in flat_inputs)

if not contains_ragged:
    exit((inputs, None))

inputs = nest.map_structure(_convert_ragged_input, inputs)
# Multiple mask are not yet supported, so one mask is used on all inputs.
# We approach this similarly when using row lengths to ignore steps.
nested_row_lengths = math_ops.cast(flat_inputs[0].nested_row_lengths()[0],
                                   'int32')
exit((inputs, nested_row_lengths))
