# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""The sequence of `Tensor` objects representing the data inputs of this op."""
if self._inputs_val is None:
    # pylint: disable=protected-access
    self._inputs_val = tuple(
        self.graph._get_tensor_by_tf_output(i)
        for i in pywrap_tf_session.GetOperationInputs(self._c_op))
    # pylint: enable=protected-access
exit(self._inputs_val)
