# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Constructs the `Distribution`.

    **This is a private method for subclass use.**

    Args:
      dtype: The type of the event samples. `None` implies no type-enforcement.
      reparameterization_type: Instance of `ReparameterizationType`.
        If `distributions.FULLY_REPARAMETERIZED`, this
        `Distribution` can be reparameterized in terms of some standard
        distribution with a function whose Jacobian is constant for the support
        of the standard distribution. If `distributions.NOT_REPARAMETERIZED`,
        then no such reparameterization is available.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`, statistics
        (e.g., mean, mode, variance) use the value "`NaN`" to indicate the
        result is undefined. When `False`, an exception is raised if one or
        more of the statistic's batch members are undefined.
      parameters: Python `dict` of parameters used to instantiate this
        `Distribution`.
      graph_parents: Python `list` of graph prerequisites of this
        `Distribution`.
      name: Python `str` name prefixed to Ops created by this class. Default:
        subclass name.

    Raises:
      ValueError: if any member of graph_parents is `None` or not a `Tensor`.
    """
graph_parents = [] if graph_parents is None else graph_parents
for i, t in enumerate(graph_parents):
    if t is None or not tensor_util.is_tf_type(t):
        raise ValueError("Graph parent item %d is not a Tensor; %s." % (i, t))
if not name or name[-1] != "/":  # `name` is not a name scope
    non_unique_name = name or type(self).__name__
    with ops.name_scope(non_unique_name) as name:
        pass
self._dtype = dtype
self._reparameterization_type = reparameterization_type
self._allow_nan_stats = allow_nan_stats
self._validate_args = validate_args
self._parameters = parameters or {}
self._graph_parents = graph_parents
self._name = name
