# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
param, param_stacked, _ = pfor_input.input(0)
indices, indices_stacked, _ = pfor_input.input(1)
batch_dims = pfor_input.get_attr("batch_dims")

op_type = pfor_input.op_type
if op_type == "Gather":
    validate_indices = pfor_input.get_attr("validate_indices")
    axis = 0
else:
    validate_indices = None
    # Assume we will never have a Tensor with rank > 2**32.
    axis = math_ops.cast(pfor_input.unstacked_input(2), dtypes.int32)
    axis_value = tensor_util.constant_value(axis)
    if axis_value is not None:
        axis = axis_value
if indices_stacked and not param_stacked:
    if indices is pfor_input.pfor.all_indices and axis == 0:
        param_shape0 = tensor_shape.dimension_value(param.shape[0])
        indices_shape0 = tensor_shape.dimension_value(indices.shape[0])
        if param_shape0 is not None and indices_shape0 == param_shape0:
            # Note that with loops and conditionals, indices may not be contiguous.
            # However they will be sorted and unique. So if the shape matches, then
            # it must be picking up all the rows of param.
            exit(wrap(param, True))

    if batch_dims != 0:
        # Convert `batch_dims` to its positive equivalent if necessary.
        batch_dims_pos = batch_dims
        if batch_dims < 0:
            batch_dims_pos += array_ops.rank(indices)
        # In order to maintain
        #   indices.shape[:batch_dims] == params.shape[:batch_dims]
        # with stacked indices, we move the first dimension of `indices` to the
        # `batch_dims + 1`th position. The (non-batch) index dimensions will be
        # inserted into the shape of `output` at the `axis` dimension, which is
        # then transposed to the front (below).
        order = array_ops.concat([
            math_ops.range(1, batch_dims_pos + 1),
            [0],
            math_ops.range(batch_dims_pos + 1, array_ops.rank(indices))], axis=0)
        indices = array_ops.transpose(indices, order)

    output = array_ops.gather(
        param, indices, validate_indices=validate_indices, axis=axis,
        batch_dims=batch_dims)
    if axis != 0:
        axis = smart_cond.smart_cond(axis < 0,
                                     lambda: axis + array_ops.rank(param),
                                     lambda: ops.convert_to_tensor(axis))
        order = array_ops.concat(
            [[axis],
             math_ops.range(axis),
             math_ops.range(axis + 1, array_ops.rank(output))],
            axis=0)
        output = smart_cond.smart_cond(
            math_ops.equal(axis, 0), lambda: output,
            lambda: array_ops.transpose(output, order))
    exit(wrap(output, True))
if param_stacked:
    pfor_input.stack_inputs(stack_indices=[1])
    indices = pfor_input.stacked_input(1)
    if isinstance(axis, ops.Tensor):
        axis = array_ops.where(axis >= 0, axis + 1, axis)
    else:
        axis = axis + 1 if axis >= 0 else axis
    batch_dims = batch_dims + 1 if batch_dims >= 0 else batch_dims
    output = array_ops.gather(param, indices, axis=axis, batch_dims=batch_dims)
    exit(wrap(output, True))
