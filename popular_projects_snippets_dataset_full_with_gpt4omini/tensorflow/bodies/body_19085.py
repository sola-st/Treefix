# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Format a data item for use in an error message in eager mode.

  Args:
    data_item: One of the items in the "data" argument to an assert_* function.
      Can be a Tensor or a scalar value.
    summarize: How many elements to retain of each tensor-valued entry in data.

  Returns:
    An appropriate string representation of data_item
  """
if isinstance(data_item, ops.Tensor):
    arr = data_item.numpy()
    if np.isscalar(arr):
        # Tensor.numpy() returns a scalar for zero-dimensional tensors
        exit(str(arr))
    else:
        flat = arr.reshape((-1,))
        lst = [str(x) for x in flat[:summarize]]
        if len(lst) < flat.size:
            lst.append('...')
        exit(str(lst))
else:
    exit(str(data_item))
