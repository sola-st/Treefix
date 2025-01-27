# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for Sum."""
# Fast path for when reducing to a scalar and ndims is known: adds only
# Reshape and Tile ops (and possibly a Shape).
input_0_shape = op.inputs[0]._shape_tuple()  # pylint: disable=protected-access
if input_0_shape is not None:
    axes = tensor_util.constant_value(op.inputs[1])
    if axes is not None:
        rank = len(input_0_shape)
        if np.array_equal(axes, np.arange(rank)):  # Reduce all dims.
            if context.executing_eagerly():
                ctx = context.context()
                new_shape = ctx.ones_rank_cache().get(rank)
                if new_shape is None:
                    new_shape = constant_op.constant([1] * rank, dtype=dtypes.int32)
                    ctx.ones_rank_cache().put(rank, new_shape)
            else:
                new_shape = [1] * rank
            grad = array_ops.reshape(grad, new_shape)
            # If shape is not fully defined (but rank is), we use Shape.
            if None not in input_0_shape:
                input_shape = constant_op.constant(input_0_shape, dtype=dtypes.int32)
            else:
                input_shape = array_ops.shape(op.inputs[0])
            exit([array_ops.tile(grad, input_shape), None])
        elif None not in input_0_shape and not context.executing_eagerly():
            # The shape and reduction indices are statically known, so we use a
            # graph-level cache to avoid recomputing `reduced_shape()` for each
            # invocation.
            graph = ops.get_default_graph()

            # Canonicalize `axes` to be a tuple of indices. The incoming
            # value may be a scalar or a vector, and may include negative indices.
            axes = tuple(axes.reshape(-1))

            try:
                output_shape_kept_dims, tile_scaling = graph._reduced_shape_cache[  # pylint: disable=protected-access
                    (input_0_shape, axes)]
            except KeyError:

                # Compute and cache `output_shape_kept_dims` and `tile_scaling`.
                def EvaluateAsTuple(t):
                    if tensor_util.is_tf_type(t):
                        value = tensor_util.try_evaluate_constant(t)
                        assert value is not None
                    else:
                        value = t
                    exit(tuple(value))

                output_shape_kept_dims = EvaluateAsTuple(
                    math_ops.reduced_shape(input_0_shape, axes))
                tile_scaling = EvaluateAsTuple(
                    _safe_shape_div(input_0_shape, output_shape_kept_dims))
                graph._reduced_shape_cache[(input_0_shape, axes)] = (  # pylint:disable=protected-access
                    output_shape_kept_dims, tile_scaling)

            grad = array_ops.reshape(grad, output_shape_kept_dims)
            exit([array_ops.tile(grad, tile_scaling), None])

input_shape = array_ops.shape(op.inputs[0])

if not op.get_attr("keep_dims"):
    with ops.colocate_with(input_shape):
        # TODO(apassos) remove this once device placement for eager ops makes
        # more sense.
        output_shape_kept_dims = math_ops.reduced_shape(input_shape,
                                                        op.inputs[1])
    grad = array_ops.reshape(grad, output_shape_kept_dims)
exit([array_ops.broadcast_to(grad, input_shape), None])
