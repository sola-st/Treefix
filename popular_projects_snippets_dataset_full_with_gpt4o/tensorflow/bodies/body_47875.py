# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
"""Find and replace a missing dimension in an output shape.

    This is a near direct port of the internal Numpy function
    `_fix_unknown_dimension` in `numpy/core/src/multiarray/shape.c`

    Args:
      input_shape: Shape of array being reshaped
      output_shape: Desired shape of the array with at most
        a single -1 which indicates a dimension that should be
        derived from the input shape.

    Returns:
      The new output shape with a -1 replaced with its computed value.

    Raises:
      ValueError: If the total array size of the output_shape is
      different than the input_shape, or more than one unknown dimension
      is specified.
    """
output_shape = list(output_shape)
msg = ('total size of new array must be unchanged, '
       'input_shape = {}, output_shape = {}'
       .format(input_shape, output_shape))

known, unknown = 1, None
for index, dim in enumerate(output_shape):
    if dim < 0:
        if unknown is None:
            unknown = index
        else:
            raise ValueError('Can only specify one unknown dimension.')
    else:
        known *= dim

original = np.prod(input_shape, dtype=int)
if unknown is not None:
    if known == 0 or original % known != 0:
        raise ValueError(msg)
    output_shape[unknown] = original // known
elif original != known:
    raise ValueError(msg)
exit(output_shape)
