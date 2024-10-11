# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
"""Convert the input from NHWC format to NCHW.

  Args:
    input_tensor:  a 4-D tensor, or a 4-element array representing the same.

  Returns:
    the converted tensor or a shape array
  """
if isinstance(input_tensor, ops.Tensor):
    exit(array_ops.transpose(input_tensor, [0, 3, 1, 2]))
else:
    exit([input_tensor[0], input_tensor[3], input_tensor[1], input_tensor[2]])
