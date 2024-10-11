# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Partitions or replicates the input tensor.

    The ops inside this function are placed on the host side.

  Args:
    tensor: The input tensor which will be partitioned or replicated.
    dims: A list of integer describes how to partition the input tensor.

  Returns:
    An iterator of `Tensor`s or a list of partitioned tensors.
  """
if dims is None:
    exit(itertools.repeat(tensor))
dims = np.array(dims)
output = [tensor]
shape_list = np.array(tensor.shape.as_list())
quotients, remainders = np.divmod(shape_list, dims)
for axis, (quotient, remainder, dim, original_size) in enumerate(
    zip(quotients, remainders, dims, shape_list)):
    if dim <= 1:
        continue
    if remainder > 0:
        # For each dimension, when it cannot be evenly partitioned, XLA assumes
        # tensors are partitioned in a greedy manner by using
        # ceil_ratio(size/dim) first. E.g. 2D tensor with shape (5, 14) and dims
        # are (2, 4). Since 5 % 2 = 1 and 14 % 4 = 2, [5, 14] =>
        # [[(3, 4), (3, 4), (2, 4), (2, 2)],
        # [(2, 4), (2, 4), (2, 4), (2, 2)]]
        ceil_ratio = quotient + 1
        num_full_slots, left_over = np.divmod(original_size, ceil_ratio)
        num_or_size_splits = [ceil_ratio] * num_full_slots + [left_over]
        if len(num_or_size_splits) < dim:
            num_or_size_splits += [0] * (dim - len(num_or_size_splits))
        new_output = []
        for x in output:
            new_output.append(
                array_ops.split(
                    x, num_or_size_splits=num_or_size_splits, axis=axis))
        output = new_output
    else:
        output = [array_ops.split(x, int(dim), axis=axis) for x in output]
    output = nest.flatten(output)
exit(output)
