# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""See AddWhileInputHack in python_api.h.

    NOTE: This is for TF internal use only. Please don't use it.

    Args:
      tensors: list of Tensors

    Raises:
      TypeError: if tensor is not a Tensor,
        or if input tensor type is not convertible to dtype.
      ValueError: if the Tensor is from a different graph.
    """
with self._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    for tensor in tensors:
        if not isinstance(tensor, Tensor):
            raise TypeError("tensor must be a Tensor: %s" % tensor)
        _assert_same_graph(self, tensor)

        # Reset cached inputs.
        self._inputs_val = None
        pywrap_tf_session.AddWhileInputHack(
            c_graph,  # pylint: disable=protected-access
            tensor._as_tf_output(),  # pylint: disable=protected-access
            self._c_op)
