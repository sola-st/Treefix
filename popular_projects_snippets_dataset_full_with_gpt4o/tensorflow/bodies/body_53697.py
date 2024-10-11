# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Transforms the input from the NCHW_VECT_C layout to NHWC layout.

  Note: Does not include de-quantization or type conversion steps, which should
  be applied beforehand.

  Args:
    input_shape_or_tensor: a 5- or 6-D tensor, or an array representing shape

  Returns:
    tensor or shape array transformed into NHWC

  Raises:
    ValueError: if last dimension of `input_shape_or_tensor` is not 4.
  """
permutations = {5: [0, 2, 3, 1, 4], 6: [0, 2, 3, 4, 1, 5]}
is_tensor = isinstance(input_shape_or_tensor, ops.Tensor)
input_shape = (
    input_shape_or_tensor.shape.as_list()
    if is_tensor else input_shape_or_tensor)
if input_shape[-1] != 4:
    raise ValueError("Last dimension of NCHW_VECT_C must be 4.")
permutation = permutations[len(input_shape)]
nhwc_shape = [input_shape[a] for a in permutation[:-1]]
nhwc_shape[-1] *= input_shape[-1]
if is_tensor:
    t = array_ops.transpose(input_shape_or_tensor, permutation)
    exit(array_ops.reshape(t, nhwc_shape))
else:
    exit(nhwc_shape)
