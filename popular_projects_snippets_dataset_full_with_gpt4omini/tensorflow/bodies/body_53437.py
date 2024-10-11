# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Update the input to this operation at the given index.

    NOTE: This is for TF internal use only. Please don't use it.

    Args:
      index: the index of the input to update.
      tensor: the Tensor to be used as the input at the given index.

    Raises:
      TypeError: if tensor is not a Tensor,
        or if input tensor type is not convertible to dtype.
      ValueError: if the Tensor is from a different graph.
    """
if not isinstance(tensor, Tensor):
    raise TypeError("tensor must be a Tensor: %s" % tensor)
_assert_same_graph(self, tensor)

# Reset cached inputs.
self._inputs_val = None
with self._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    pywrap_tf_session.UpdateEdge(
        c_graph,
        tensor._as_tf_output(),  # pylint: disable=protected-access
        self._tf_input(index))
