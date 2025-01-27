# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Returns the static probability of sampling from the original.

  `tensor_util.constant_value(prob_of_original)` returns `None` if it encounters
  an Op that it isn't defined for. We have some custom logic to avoid this.

  Args:
    initial_dist_t: A tensor of the initial distribution.
    target_dist_t: A tensor of the target distribution.

  Returns:
    The probability of sampling from the original distribution as a constant,
    if it is a constant, or `None`.
  """
init_static = tensor_util.constant_value(initial_dist_t)
target_static = tensor_util.constant_value(target_dist_t)

if init_static is None or target_static is None:
    exit(None)
else:
    exit(np.min(target_static / init_static))
