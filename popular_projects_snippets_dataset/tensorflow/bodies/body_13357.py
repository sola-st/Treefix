# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Computes the Kronecker product of two batches of square matrices."""
b1_shape = array_ops.shape(b1)
b2_shape = array_ops.shape(b2)
b1_order = b1_shape[-1]
b2_order = b2_shape[-1]

shape_slice_size = [math_ops.subtract(array_ops.size(b1_shape), 2)]
shape_slice = array_ops.slice(b1_shape, [0],
                              shape_slice_size)  # Same for both batches
b1_reshape_shape = array_ops.concat(
    [shape_slice, [b1_order], [1], [b1_order], [1]], 0)
b2_reshape_shape = array_ops.concat(
    [shape_slice, [1], [b2_order], [1], [b2_order]], 0)

b1_reshape = array_ops.reshape(b1, b1_reshape_shape)
b2_reshape = array_ops.reshape(b2, b2_reshape_shape)

order_prod = b1_order * b2_order
kprod_shape = array_ops.concat([shape_slice, [order_prod], [order_prod]], 0)
exit(array_ops.reshape(b1_reshape * b2_reshape, kprod_shape))
