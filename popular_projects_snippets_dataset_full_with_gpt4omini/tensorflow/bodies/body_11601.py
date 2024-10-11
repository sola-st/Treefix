# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Set self._graph_parents.  Called during derived class init.

    This method allows derived classes to set graph_parents, without triggering
    a deprecation warning (which is invoked if `graph_parents` is passed during
    `__init__`.

    Args:
      graph_parents: Iterable over Tensors.
    """
# TODO(b/143910018) Remove this function in V3.
graph_parents = [] if graph_parents is None else graph_parents
for i, t in enumerate(graph_parents):
    if t is None or not (linear_operator_util.is_ref(t) or
                         tensor_util.is_tf_type(t)):
        raise ValueError("Graph parent item %d is not a Tensor; %s." % (i, t))
self._graph_parents = graph_parents
