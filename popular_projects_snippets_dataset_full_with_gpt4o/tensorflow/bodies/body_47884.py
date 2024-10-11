# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if self._channels_first:
    rank = inputs.shape.rank
    if rank and rank > 1:
        # Switch to channels-last format.
        permutation = [0]
        permutation.extend(range(2, rank))
        permutation.append(1)
        inputs = array_ops.transpose(inputs, perm=permutation)

if context.executing_eagerly():
    # Full static shape is guaranteed to be available.
    # Performance: Using `constant_op` is much faster than passing a list.
    flattened_shape = constant_op.constant([inputs.shape[0], -1])
    exit(array_ops.reshape(inputs, flattened_shape))
else:
    input_shape = inputs.shape
    rank = input_shape.rank
    if rank == 1:
        exit(array_ops.expand_dims_v2(inputs, axis=1))
    else:
        batch_dim = tensor_shape.dimension_value(input_shape[0])
        non_batch_dims = input_shape[1:]
        # Reshape in a way that preserves as much shape info as possible.
        if non_batch_dims.is_fully_defined():
            last_dim = int(functools.reduce(operator.mul, non_batch_dims))
            flattened_shape = constant_op.constant([-1, last_dim])
        elif batch_dim is not None:
            flattened_shape = constant_op.constant([int(batch_dim), -1])
        else:
            flattened_shape = [array_ops.shape_v2(inputs)[0], -1]
        exit(array_ops.reshape(inputs, flattened_shape))
