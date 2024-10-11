# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Fallback implementation that supports summing an index over > 2 inputs."""
inputs = list(inputs)
input_shapes = [x.shape for x in inputs]
idx_in, idx_out = _einsum_v1_parse_and_resolve_equation(
    equation, input_shapes)

idx_all = set(''.join(idx_in) + idx_out)
indices = ''.join(sorted(idx_all))

missing_idx = set(idx_out).difference(idx_all)
if missing_idx:
    raise ValueError(f'Unknown output axes: {missing_idx}.')

axis_order = {}
for ax in indices:
    if ax not in idx_out:
        axis_order[ax] = len(axis_order)
for ax in idx_out:
    axis_order[ax] = len(axis_order)

# transpose inputs so axes are in order
for i, (input_, axes_) in enumerate(zip(inputs, idx_in)):
    if input_.shape.ndims != len(axes_):
        raise ValueError(
            f'Input {i} with axes {axes_} has incorrect number of dimensions '
            f'(expected {len(axes_)}, got {input_.shape.ndims}).')

    sorted_idx = sorted(axes_, key=axis_order.get)

    if len(set(axes_)) != len(axes_):
        raise ValueError(
            f'Subscript not supported: an axis appears more than once: {axes_}.')

    if list(axes_) != sorted_idx:
        permuted = [axes_.find(ax) for ax in sorted_idx]
        inputs[i] = array_ops.transpose(input_, permuted)
        idx_in[i] = sorted_idx

reduction_idx = []
shapes = [[dim if dim else -1
           for dim in tensor.shape.as_list()]
          for tensor in inputs]

# validate shapes for broadcasting
for j, ax in enumerate(sorted(idx_all, key=axis_order.get)):
    dims = []
    for i, idx in enumerate(idx_in):
        if ax not in idx:
            shapes[i].insert(j, 1)
        else:
            dim = shapes[i][j]
            if isinstance(dim, int) and dim > 1:
                dims.append(dim)

    if len(set(dims)) > 1:
        raise ValueError(f'Dimension mismatch on axis: {ax}. '
                         f'Found {len(set(dims))}, expected 1.')

    if ax not in idx_out:
        reduction_idx.append(j)

  # reshape, multiply
expanded_inputs = [
    array_ops.reshape(input_, shape) for input_, shape in zip(inputs, shapes)
]
expanded_output = 1
for input_ in expanded_inputs:
    expanded_output *= input_

# contract
exit(math_ops.reduce_sum(expanded_output, reduction_idx))
