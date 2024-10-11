# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker.py
"""Computes the numeric Jacobian for dy/dx.

  Computes the numeric Jacobian by slightly perturbing the inputs and
  measuring the differences on the output.

  Args:
    x: the tensor "x".
    x_shape: the dimensions of x as a tuple or an array of ints.
    x_data: a numpy array as the input data for x
    y: the tensor "y".
    y_shape: the dimensions of y as a tuple or an array of ints.
    delta: the amount of perturbation we give to the input
    extra_feed_dict: dict that allows fixing specified tensor values
      during the jacobian calculation.

  Returns:
    A 2-d numpy array representing the Jacobian for dy/dx. It has "x_size" rows
    and "y_size" columns where "x_size" is the number of elements in x and
    "y_size" is the number of elements in y.
  """
# bfloat16 doesn't have enough bits to represent high precision numbers such
# as delta. Convert to float32 here. Since numeric_jacobian is expected to
# be the groundtruth to compare against, it shouldn't lose any information.
if x.dtype == dtypes.bfloat16:
    x = math_ops.cast(x, dtypes.float32)  # TODO(wangpeng): Now that the new x
            # is an output of the old x, isn't feeding to the new x a mistake?
if y.dtype == dtypes.bfloat16:
    y = math_ops.cast(y, dtypes.float32)
if x_data.dtype == dtypes.bfloat16.as_numpy_dtype:
    x_data = x_data.astype(np.float32)

# To compute the jacobian, we treat x and y as one-dimensional vectors
x_size = _product(x_shape) * (2 if x.dtype.is_complex else 1)
y_size = _product(y_shape) * (2 if y.dtype.is_complex else 1)
x_dtype = x.dtype.real_dtype.as_numpy_dtype
y_dtype = y.dtype.real_dtype.as_numpy_dtype

# Make sure we have the right types
x_data = np.asarray(x_data, dtype=x.dtype.as_numpy_dtype)
scale = np.asarray(2 * delta, dtype=y_dtype)[()]

jacobian = np.zeros((x_size, y_size), dtype=x_dtype)
# For each of the entry of x, we slightly perturbs this by adding and
# subtracting a delta and then compute difference between the outputs. This
# will give us one row of the Jacobian matrix.
for row in range(x_size):
    x_pos = x_data.copy()
    x_neg = x_data.copy()
    x_pos.ravel().view(x_dtype)[row] += delta
    y_pos = y.eval(feed_dict=_extra_feeds(extra_feed_dict, {x: x_pos}))
    x_neg.ravel().view(x_dtype)[row] -= delta
    y_neg = y.eval(feed_dict=_extra_feeds(extra_feed_dict, {x: x_neg}))
    diff = (y_pos - y_neg) / scale
    jacobian[row, :] = diff.ravel().view(y_dtype)

logging.vlog(1, "Numeric Jacobian =\n%s", jacobian)
exit(jacobian)
