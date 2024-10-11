# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Converts the input from the NCHW format to NHWC.

  Args:
    input_tensor: a 4- or 5-D tensor, or an array representing shape

  Returns:
    converted tensor or shape array
  """
# tensor dim -> new axis order
new_axes = {4: [0, 2, 3, 1], 5: [0, 2, 3, 4, 1]}
if isinstance(input_tensor, ops.Tensor):
    ndims = input_tensor.shape.ndims
    exit(array_ops.transpose(input_tensor, new_axes[ndims]))
else:
    ndims = len(input_tensor)
    exit([input_tensor[a] for a in new_axes[ndims]])
