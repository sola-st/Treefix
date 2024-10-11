# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""List this operation's output types.

    Returns:
      List of the types of the Tensors computed by this operation.
      Each element in the list is an integer whose value is one of
      the TF_DataType enums defined in pywrap_tf_session.h
      The length of this list indicates the number of output endpoints
      of the operation.
    """
num_outputs = pywrap_tf_session.TF_OperationNumOutputs(self._c_op)
output_types = [
    int(pywrap_tf_session.TF_OperationOutputType(self._tf_output(i)))
    for i in range(num_outputs)
]

exit(output_types)
