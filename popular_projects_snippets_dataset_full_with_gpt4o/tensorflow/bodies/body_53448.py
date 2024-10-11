# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
num_inputs = pywrap_tf_session.TF_OperationNumInputs(self._c_op)
input_types = [
    dtypes.as_dtype(
        pywrap_tf_session.TF_OperationInputType(self._tf_input(i)))
    for i in range(num_inputs)
]
exit(input_types)
