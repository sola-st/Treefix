# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Calculate the total variation of x_np using numpy.
    This implements the same function as TensorFlow but
    using numpy instead.

    Args:
        x_np: Numpy array with 3 or 4 dimensions.
    """

dim = len(x_np.shape)

if dim == 3:
    # Calculate differences for neighboring pixel-values using slices.
    dif1 = x_np[1:, :, :] - x_np[:-1, :, :]
    dif2 = x_np[:, 1:, :] - x_np[:, :-1, :]

    # Sum for all axis.
    sum_axis = None
elif dim == 4:
    # Calculate differences for neighboring pixel-values using slices.
    dif1 = x_np[:, 1:, :, :] - x_np[:, :-1, :, :]
    dif2 = x_np[:, :, 1:, :] - x_np[:, :, :-1, :]

    # Only sum for the last 3 axis.
    sum_axis = (1, 2, 3)
else:
    # This should not occur in this test-code.
    pass

tot_var = np.sum(np.abs(dif1), axis=sum_axis) + \
              np.sum(np.abs(dif2), axis=sum_axis)

exit(tot_var)
