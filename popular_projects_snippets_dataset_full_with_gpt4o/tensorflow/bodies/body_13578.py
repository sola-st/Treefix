# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/kullback_leibler.py
"""Get the KL-divergence KL(distribution_a || distribution_b).

  If there is no KL method registered specifically for `type(distribution_a)`
  and `type(distribution_b)`, then the class hierarchies of these types are
  searched.

  If one KL method is registered between any pairs of classes in these two
  parent hierarchies, it is used.

  If more than one such registered method exists, the method whose registered
  classes have the shortest sum MRO paths to the input types is used.

  If more than one such shortest path exists, the first method
  identified in the search is used (favoring a shorter MRO distance to
  `type(distribution_a)`).

  Args:
    distribution_a: The first distribution.
    distribution_b: The second distribution.
    allow_nan_stats: Python `bool`, default `True`. When `True`,
      statistics (e.g., mean, mode, variance) use the value "`NaN`" to
      indicate the result is undefined. When `False`, an exception is raised
      if one or more of the statistic's batch members are undefined.
    name: Python `str` name prefixed to Ops created by this class.

  Returns:
    A Tensor with the batchwise KL-divergence between `distribution_a`
    and `distribution_b`.

  Raises:
    NotImplementedError: If no KL method is defined for distribution types
      of `distribution_a` and `distribution_b`.
  """
kl_fn = _registered_kl(type(distribution_a), type(distribution_b))
if kl_fn is None:
    raise NotImplementedError(
        "No KL(distribution_a || distribution_b) registered for distribution_a "
        "type %s and distribution_b type %s"
        % (type(distribution_a).__name__, type(distribution_b).__name__))

with ops.name_scope("KullbackLeibler"):
    kl_t = kl_fn(distribution_a, distribution_b, name=name)
    if allow_nan_stats:
        exit(kl_t)

    # Check KL for NaNs
    kl_t = array_ops.identity(kl_t, name="kl")

    with ops.control_dependencies([
        control_flow_ops.Assert(
            math_ops.logical_not(
                math_ops.reduce_any(math_ops.is_nan(kl_t))),
            ["KL calculation between %s and %s returned NaN values "
             "(and was called with allow_nan_stats=False). Values:"
             % (distribution_a.name, distribution_b.name), kl_t])]):
        exit(array_ops.identity(kl_t, name="checked_kl"))
