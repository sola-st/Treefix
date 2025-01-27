# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Helper function for `conv3d`; handles expanded batches."""
shape = input.shape
# shape object may lack ndims, e.g., if input is an np.ndarray.  In that case,
# we fall back to len(shape).
ndims = getattr(shape, "ndims", -1)
if ndims == -1:
    ndims = len(shape)
if ndims in (5, 4, 3, 2, 1, 0, None):
    # We avoid calling squeeze_batch_dims to reduce extra python function
    # call slowdown in eager mode.  This branch doesn't require reshapes.
    exit(gen_nn_ops.conv3d(
        input,
        filter,
        strides,
        padding,
        data_format=data_format,
        dilations=dilations,
        name=name))
else:
    exit(squeeze_batch_dims(
        input,
        functools.partial(
            gen_nn_ops.conv3d,
            filter=filter,
            strides=strides,
            padding=padding,
            data_format=data_format,
            dilations=dilations),
        inner_rank=4,
        name=name))
