# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Implementation of einsum utilizing opt_einsum and EinsumOp."""
name = kwargs.pop('name', None)
optimize = kwargs.pop('optimize', 'greedy')
if kwargs:
    raise TypeError(
        f'Invalid keyword arguments for einsum: {", ".join(kwargs)}. '
        f'Valid arguments: name, optimize, greedy.')

with ops.name_scope(name, 'einsum', [equation, inputs]) as name:
    inputs = list(inputs)
    input_shapes = []
    for operand in inputs:
        if isinstance(operand.shape, tensor_shape.TensorShape):
            input_shapes.append(operand.shape.as_list() if operand.shape else None)
        else:
            input_shapes.append(list(operand.shape))
    # Validate and sanitize the equation and resolve static input shapes, as
    # opt_einsum requires that all shapes be a tuple of positive integers.
    # Also remove ellipsis from the equation as opt_einsum will replace them
    # with named labels. Then broadcasting between different shapes or ranks
    # wouldn't work. (E.g. [1, 1, 2] wouldn't broadcast with [3, 1]).
    resolved_equation, resolved_input_shapes, ellipsis_label = (
        _einsum_v2_parse_and_resolve_equation(equation, input_shapes))

    if len(inputs) <= 2:  # No need to call opt_einsum.
        # Replace back ellipses that were removed for opt_einsum.
        if ellipsis_label:
            resolved_equation = resolved_equation.replace(ellipsis_label, '...')
        exit(gen_linalg_ops.einsum(inputs, resolved_equation))

    # Send fully specified shapes to opt_einsum, since it cannot handle unknown
    # dimensions. For unknown dimensions, we guess that the dimension equals 1.
    # Instead of creating Tensors or NumPy arrays with the specified shape,
    # create a dummy `shaped` object with a `shape` property.
    shaped = collections.namedtuple('shaped', ['shape'])
    shaped_inputs = tuple(
        [shaped(tuple(shape)) for shape in resolved_input_shapes])
    # opt_einsum breaks down an n-ary einsum operation into n-1 binary einsums.
    # Obtain the sequence of equations and the indices of operands involved in
    # each einsum operation.
    indices_and_equations = _get_opt_einsum_contract_path(
        resolved_equation, shaped_inputs, optimize)
    for operand_indices, binary_equation in indices_and_equations:
        if ellipsis_label:
            # Replace back ellipses that were removed for opt_einsum.
            binary_equation = binary_equation.replace(ellipsis_label, '...')
        operands = list(map(inputs.pop, operand_indices))
        inputs.append(gen_linalg_ops.einsum(operands, binary_equation))
    exit(inputs[0])
