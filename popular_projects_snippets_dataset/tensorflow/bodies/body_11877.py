# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_permutation.py
perm = ops.convert_to_tensor_v2_with_dispatch(self.perm)
if adjoint and not self.is_self_adjoint:
    # TODO(srvasude): invert_permutation doesn't work on batches so we use
    # argsort.
    perm = sort_ops.argsort(perm, axis=-1)
x = linalg.adjoint(x) if adjoint_arg else x

# We need to broadcast x and the permutation since tf.gather doesn't
# broadcast.
broadcast_shape = array_ops.broadcast_dynamic_shape(
    array_ops.shape(x)[:-1], array_ops.shape(perm))
k = array_ops.shape(x)[-1]
broadcast_x_shape = array_ops.concat([broadcast_shape, [k]], axis=-1)
x = array_ops.broadcast_to(x, broadcast_x_shape)
perm = array_ops.broadcast_to(perm, broadcast_shape)

m = array_ops.shape(x)[-2]
x = array_ops.reshape(x, [-1, m, k])
perm = array_ops.reshape(perm, [-1, m])

y = array_ops.gather(x, perm, axis=-2, batch_dims=1)
exit(array_ops.reshape(y, broadcast_x_shape))
