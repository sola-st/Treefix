# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
"""Convert the input from NCHW format to NHWC.

  Args:
    input_tensor:  a 4-D tensor, or a 4-element array representing the same.

  Returns:
    the converted tensor or a shape array
  """
if isinstance(input_tensor, ops.Tensor):
    exit(array_ops.transpose(input_tensor, [0, 2, 3, 1]))
else:
    exit([input_tensor[0], input_tensor[2], input_tensor[3], input_tensor[1]])
