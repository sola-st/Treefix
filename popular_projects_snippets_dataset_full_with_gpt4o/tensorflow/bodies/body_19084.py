# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Subroutine of _binary_assert that generates the components of the default error message when running in eager mode.

  Args:
    sym: Mathematical symbol for the test to apply to pairs of tensor elements,
      i.e. "=="
    x: First input to the assertion after applying `convert_to_tensor()`
    y: Second input to the assertion
    summarize: Value of the "summarize" parameter to the original assert_* call;
      tells how many elements of each tensor to print.
    test_op: TensorFlow op that returns a Boolean tensor with True in each
      position where the assertion is satisfied.

  Returns:
    List of tensors and scalars that, when stringified and concatenated,
    will produce the error message string.
  """
# Prepare a message with first elements of x and y.
data = []

data.append('Condition x %s y did not hold.' % sym)

if summarize > 0:
    if x.shape == y.shape and x.shape.as_list():
        # If the shapes of x and y are the same (and not scalars),
        # Get the values that actually differed and their indices.
        # If shapes are different this information is more confusing
        # than useful.
        mask = math_ops.logical_not(test_op)
        indices = array_ops.where(mask)
        indices_np = indices.numpy()
        x_vals = array_ops.boolean_mask(x, mask)
        y_vals = array_ops.boolean_mask(y, mask)
        num_vals = min(summarize, indices_np.shape[0])
        data.append('Indices of first %d different values:' % num_vals)
        data.append(indices_np[:num_vals])
        data.append('Corresponding x values:')
        data.append(x_vals.numpy().reshape((-1,))[:num_vals])
        data.append('Corresponding y values:')
        data.append(y_vals.numpy().reshape((-1,))[:num_vals])

    # reshape((-1,)) is the fastest way to get a flat array view.
    x_np = x.numpy().reshape((-1,))
    y_np = y.numpy().reshape((-1,))
    x_sum = min(x_np.size, summarize)
    y_sum = min(y_np.size, summarize)
    data.append('First %d elements of x:' % x_sum)
    data.append(x_np[:x_sum])
    data.append('First %d elements of y:' % y_sum)
    data.append(y_np[:y_sum])

exit(data)
