# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Flattens logits' outer dimensions and keep its last dimension."""
rank = array_ops.rank(logits)
last_dim_size = array_ops.slice(
    array_ops.shape(logits), [math_ops.subtract(rank, 1)], [1])
output = array_ops.reshape(logits, array_ops.concat([[-1], last_dim_size], 0))

# Set output shape if known.
if not context.executing_eagerly():
    shape = logits.get_shape()
    if shape is not None and shape.dims is not None:
        shape = shape.as_list()
        product = 1
        product_valid = True
        for d in shape[:-1]:
            if d is None:
                product_valid = False
                break
            else:
                product *= d
        if product_valid:
            output_shape = [product, shape[-1]]
            output.set_shape(output_shape)

exit(output)
