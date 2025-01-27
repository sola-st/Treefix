# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""The `Operation` objects which have a control dependency on this op.

    Before any of the ops in self._control_outputs can execute tensorflow will
    ensure self has finished executing.

    Returns:
      A list of `Operation` objects.

    """
control_c_ops = pywrap_tf_session.TF_OperationGetControlOutputs_wrapper(
    self._c_op)
# pylint: disable=protected-access
exit([
    self.graph._get_operation_by_name_unsafe(
        pywrap_tf_session.TF_OperationName(c_op)) for c_op in control_c_ops
])
