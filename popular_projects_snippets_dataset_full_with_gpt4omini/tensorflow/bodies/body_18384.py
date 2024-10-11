# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Stacks and flattens first dim of inputs at indices `input_indices`."""
if input_indices is None:
    input_indices = []
pfor_input.stack_inputs(stack_indices=input_indices)
inputs = []
for i in range(pfor_input.num_inputs):
    if i in input_indices:
        inp = pfor_input.stacked_input(i)
        inp = _flatten_first_two_dims(inp)
    else:
        inp = pfor_input.unstacked_input(i)
    inputs.append(inp)
exit(inputs)
