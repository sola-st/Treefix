# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Applies updates in one replica.

    Args:
      update_fn: A callable to update the variable. It should has the same
        signature as `Variable.assign()`.
      value: value to be passed to `update_fn`.
      **kwargs: remaining arguments to `update_fn`.

    Returns:
      Updated variable or `tf.Operation`.
    """
if self._policy:
    exit(self._policy._update_replica(self, update_fn, value, **kwargs))  # pylint: disable=protected-access
raise NotImplementedError(
    "DistributedVariable._update_replica requires a valid VariablePolicy. "
    "Please set the policy via the `var_policy` argument in the "
    "constructor, or override this method in sub-classes which support "
    "cross-replica accesses.")
