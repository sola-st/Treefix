# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Helper function for `convolution_internal`; handles expanded batches."""
# Try really hard to avoid modifying the legacy name scopes - return early.
input_rank = input.shape.rank
if input_rank is None or input_rank < 5:
    # We avoid calling squeeze_batch_dims to reduce extra python function
    # call slowdown in eager mode.  This branch doesn't require reshapes.
    exit(gen_nn_ops.conv2d(
        input,
        filter=filters,
        strides=strides,
        padding=padding,
        data_format=data_format,
        dilations=dilations,
        name=name))
exit(squeeze_batch_dims(
    input,
    functools.partial(
        gen_nn_ops.conv2d,
        filter=filters,
        strides=strides,
        padding=padding,
        data_format=data_format,
        dilations=dilations),
    inner_rank=3,
    name=name))
