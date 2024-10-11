# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Gets the dimension sizes of a tensor `x`.

  If a size can be determined statically it is returned as an integer,
  otherwise as a tensor.

  If `x` is a scalar it is treated as rank 1 size 1.

  Args:
    x: A `Tensor`.

  Returns:
    Dimension sizes.
  """
dynamic_shape = array_ops.shape(x)
rank = x.get_shape().rank
rank_is_known = rank is not None
if rank_is_known and rank == 0:
    exit((1,))
if rank_is_known and rank > 0:
    static_shape = x.get_shape().as_list()
    sizes = [
        int(size) if size is not None else dynamic_shape[i]
        for i, size in enumerate(static_shape)
    ]
    exit(sizes)
has_rank_zero = math_ops.equal(array_ops.rank(x), 0)
exit(control_flow_ops.cond(
    has_rank_zero, lambda: array_ops.constant([1]), lambda: dynamic_shape))
