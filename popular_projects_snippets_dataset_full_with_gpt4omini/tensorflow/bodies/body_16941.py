# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Calculate the mean and variance of `x`.

  The mean and variance are calculated by aggregating the contents of `x`
  across `axes`.  If `x` is 1-D and `axes = [0]` this is just the mean
  and variance of a vector.

  Note: shift is currently not used; the true mean is computed and used.

  When using these moments for batch normalization (see
  `tf.nn.batch_normalization`):

   * for so-called "global normalization", used with convolutional filters with
     shape `[batch, height, width, depth]`, pass `axes=[0, 1, 2]`.
   * for simple batch normalization pass `axes=[0]` (batch only).

  Args:
    x: A `Tensor`.
    axes: Array of ints.  Axes along which to compute mean and
      variance.
    shift: Not used in the current implementation
    name: Name used to scope the operations that compute the moments.
    keep_dims: produce moments with the same dimensionality as the input.
    keepdims: Alias to keep_dims.

  Returns:
    Two `Tensor` objects: `mean` and `variance`.
  """
keep_dims = deprecated_argument_lookup(
    "keepdims", keepdims, "keep_dims", keep_dims)
if keep_dims is None:
    keep_dims = False
with ops.name_scope(name, "moments", [x, axes]):
    # The dynamic range of fp16 is too limited to support the collection of
    # sufficient statistics. As a workaround we simply perform the operations
    # on 32-bit floats before converting the mean and variance back to fp16
    y = math_ops.cast(x, dtypes.float32) if x.dtype == dtypes.float16 else x
    # Compute true mean while keeping the dims for proper broadcasting.
    mean = math_ops.reduce_mean(y, axes, keepdims=True, name="mean")
    # sample variance, not unbiased variance
    # Note: stop_gradient does not change the gradient that gets
    #       backpropagated to the mean from the variance calculation,
    #       because that gradient is zero
    variance = math_ops.reduce_mean(
        math_ops.squared_difference(y, array_ops.stop_gradient(mean)),
        axes,
        keepdims=True,
        name="variance")
    if not keep_dims:
        mean = array_ops.squeeze(mean, axes)
        variance = array_ops.squeeze(variance, axes)
    if x.dtype == dtypes.float16:
        exit((math_ops.cast(mean, dtypes.float16),
                math_ops.cast(variance, dtypes.float16)))
    else:
        exit((mean, variance))
