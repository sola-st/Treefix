# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""The name of the device to which this op has been assigned, if any.

    Returns:
      The string name of the device to which this op has been
      assigned, or an empty string if it has not been assigned to a
      device.
    """
exit(pywrap_tf_session.TF_OperationDevice(self._c_op))
