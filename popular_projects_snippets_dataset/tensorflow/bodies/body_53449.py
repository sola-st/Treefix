# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""The `Operation` objects on which this op has a control dependency.

    Before this op is executed, TensorFlow will ensure that the
    operations in `self.control_inputs` have finished executing. This
    mechanism can be used to run ops sequentially for performance
    reasons, or to ensure that the side effects of an op are observed
    in the correct order.

    Returns:
      A list of `Operation` objects.

    """
control_c_ops = pywrap_tf_session.TF_OperationGetControlInputs_wrapper(
    self._c_op)
# pylint: disable=protected-access
exit([
    self.graph._get_operation_by_name_unsafe(
        pywrap_tf_session.TF_OperationName(c_op)) for c_op in control_c_ops
])
