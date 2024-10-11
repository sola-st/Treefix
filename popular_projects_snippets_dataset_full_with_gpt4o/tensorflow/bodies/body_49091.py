# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Batchwise dot product.

  `batch_dot` is used to compute dot product of `x` and `y` when
  `x` and `y` are data in batch, i.e. in a shape of
  `(batch_size, :)`.
  `batch_dot` results in a tensor or variable with less dimensions
  than the input. If the number of dimensions is reduced to 1,
  we use `expand_dims` to make sure that ndim is at least 2.

  Args:
    x: Keras tensor or variable with `ndim >= 2`.
    y: Keras tensor or variable with `ndim >= 2`.
    axes: Tuple or list of integers with target dimensions, or single integer.
      The sizes of `x.shape[axes[0]]` and `y.shape[axes[1]]` should be equal.

  Returns:
    A tensor with shape equal to the concatenation of `x`'s shape
    (less the dimension that was summed over) and `y`'s shape
    (less the batch dimension and the dimension that was summed over).
    If the final rank is 1, we reshape it to `(batch_size, 1)`.

  Examples:

  >>> x_batch = tf.keras.backend.ones(shape=(32, 20, 1))
  >>> y_batch = tf.keras.backend.ones(shape=(32, 30, 20))
  >>> xy_batch_dot = tf.keras.backend.batch_dot(x_batch, y_batch, axes=(1, 2))
  >>> tf.keras.backend.int_shape(xy_batch_dot)
  (32, 1, 30)

  Shape inference:
    Let `x`'s shape be `(100, 20)` and `y`'s shape be `(100, 30, 20)`.
    If `axes` is (1, 2), to find the output shape of resultant tensor,
        loop through each dimension in `x`'s shape and `y`'s shape:
    * `x.shape[0]` : 100 : append to output shape
    * `x.shape[1]` : 20 : do not append to output shape,
        dimension 1 of `x` has been summed over. (`dot_axes[0]` = 1)
    * `y.shape[0]` : 100 : do not append to output shape,
        always ignore first dimension of `y`
    * `y.shape[1]` : 30 : append to output shape
    * `y.shape[2]` : 20 : do not append to output shape,
        dimension 2 of `y` has been summed over. (`dot_axes[1]` = 2)
    `output_shape` = `(100, 30)`
  """
x_shape = int_shape(x)
y_shape = int_shape(y)

x_ndim = len(x_shape)
y_ndim = len(y_shape)

if x_ndim < 2 or y_ndim < 2:
    raise ValueError('Cannot do batch_dot on inputs '
                     'with rank < 2. '
                     'Received inputs with shapes ' +
                     str(x_shape) + ' and ' +
                     str(y_shape) + '.')

x_batch_size = x_shape[0]
y_batch_size = y_shape[0]

if x_batch_size is not None and y_batch_size is not None:
    if x_batch_size != y_batch_size:
        raise ValueError('Cannot do batch_dot on inputs '
                         'with different batch sizes. '
                         'Received inputs with shapes ' +
                         str(x_shape) + ' and ' +
                         str(y_shape) + '.')
if isinstance(axes, int):
    axes = [axes, axes]

if axes is None:
    if y_ndim == 2:
        axes = [x_ndim - 1, y_ndim - 1]
    else:
        axes = [x_ndim - 1, y_ndim - 2]

if py_any(isinstance(a, (list, tuple)) for a in axes):
    raise ValueError('Multiple target dimensions are not supported. ' +
                     'Expected: None, int, (int, int), ' +
                     'Provided: ' + str(axes))

# if tuple, convert to list.
axes = list(axes)

# convert negative indices.
if axes[0] < 0:
    axes[0] += x_ndim
if axes[1] < 0:
    axes[1] += y_ndim

# sanity checks
if 0 in axes:
    raise ValueError('Cannot perform batch_dot over axis 0. '
                     'If your inputs are not batched, '
                     'add a dummy batch dimension to your '
                     'inputs using K.expand_dims(x, 0)')
a0, a1 = axes
d1 = x_shape[a0]
d2 = y_shape[a1]

if d1 is not None and d2 is not None and d1 != d2:
    raise ValueError('Cannot do batch_dot on inputs with shapes ' +
                     str(x_shape) + ' and ' + str(y_shape) +
                     ' with axes=' + str(axes) + '. x.shape[%d] != '
                     'y.shape[%d] (%d != %d).' % (axes[0], axes[1], d1, d2))

# backup ndims. Need them later.
orig_x_ndim = x_ndim
orig_y_ndim = y_ndim

# if rank is 2, expand to 3.
if x_ndim == 2:
    x = array_ops.expand_dims(x, 1)
    a0 += 1
    x_ndim += 1
if y_ndim == 2:
    y = array_ops.expand_dims(y, 2)
    y_ndim += 1

# bring x's dimension to be reduced to last axis.
if a0 != x_ndim - 1:
    pattern = list(range(x_ndim))
    for i in range(a0, x_ndim - 1):
        pattern[i] = pattern[i + 1]
    pattern[-1] = a0
    x = array_ops.transpose(x, pattern)

# bring y's dimension to be reduced to axis 1.
if a1 != 1:
    pattern = list(range(y_ndim))
    for i in range(a1, 1, -1):
        pattern[i] = pattern[i - 1]
    pattern[1] = a1
    y = array_ops.transpose(y, pattern)

# normalize both inputs to rank 3.
if x_ndim > 3:
    # squash middle dimensions of x.
    x_shape = shape(x)
    x_mid_dims = x_shape[1:-1]
    x_squashed_shape = array_ops.stack(
        [x_shape[0], -1, x_shape[-1]])
    x = array_ops.reshape(x, x_squashed_shape)
    x_squashed = True
else:
    x_squashed = False

if y_ndim > 3:
    # squash trailing dimensions of y.
    y_shape = shape(y)
    y_trail_dims = y_shape[2:]
    y_squashed_shape = array_ops.stack(
        [y_shape[0], y_shape[1], -1])
    y = array_ops.reshape(y, y_squashed_shape)
    y_squashed = True
else:
    y_squashed = False

result = math_ops.matmul(x, y)

# if inputs were squashed, we have to reshape the matmul output.
output_shape = array_ops.shape(result)
do_reshape = False

if x_squashed:
    output_shape = array_ops.concat(
        [output_shape[:1],
         x_mid_dims,
         output_shape[-1:]], 0)
    do_reshape = True

if y_squashed:
    output_shape = array_ops.concat([output_shape[:-1], y_trail_dims], 0)
    do_reshape = True

if do_reshape:
    result = array_ops.reshape(result, output_shape)

# if the inputs were originally rank 2, we remove the added 1 dim.
if orig_x_ndim == 2:
    result = array_ops.squeeze(result, 1)
elif orig_y_ndim == 2:
    result = array_ops.squeeze(result, -1)

exit(result)
