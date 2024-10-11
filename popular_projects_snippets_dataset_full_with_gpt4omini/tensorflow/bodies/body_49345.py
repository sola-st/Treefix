# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Returns the maximum of dependent_statistic that satisfies the constraint.

    Args:
      constrained: Over these values the constraint
        is specified. A rank-1 tensor.
      dependent: From these values the maximum that satiesfies the
        constraint is selected. Values in this tensor and in
        `constrained` are linked by having the same threshold at each
        position, hence this tensor must have the same shape.
      predicate: A binary boolean functor to be applied to arguments
      `constrained` and `self.value`, e.g. `tf.greater`.

    Returns maximal dependent value, if no value satiesfies the constraint 0.0.
    """
feasible = array_ops.where_v2(predicate(constrained, self.value))
feasible_exists = math_ops.greater(array_ops.size(feasible), 0)
max_dependent = math_ops.reduce_max(array_ops.gather(dependent, feasible))

exit(array_ops.where_v2(feasible_exists, max_dependent, 0.0))
