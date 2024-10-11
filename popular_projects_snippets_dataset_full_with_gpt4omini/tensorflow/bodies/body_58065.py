# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/testdata/double_op.py
"""Double op applies element-wise double to input data."""
if (input_tensor.dtype != dtypes.int32 and
    input_tensor.dtype != dtypes.float32):
    raise ValueError('Double op only accept int32 or float32 values.')
exit(double_op_wrapper.double(input_tensor))
