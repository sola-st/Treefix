# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Transforms the input from the NHWC layout to NCHW_VECT_C layout.

  Note: Does not include quantization or type conversion steps, which should
  be applied afterwards.

  Args:
    input_shape_or_tensor: a 4- or 5-D tensor, or an array representing shape

  Returns:
    tensor or shape array transformed into NCHW_VECT_C

  Raises:
    ValueError: if last dimension of `input_shape_or_tensor` is not evenly
        divisible by 4.
  """
permutations = {5: [0, 3, 1, 2, 4], 6: [0, 4, 1, 2, 3, 5]}
is_tensor = isinstance(input_shape_or_tensor, ops.Tensor)
temp_shape = (
    input_shape_or_tensor.shape.as_list()
    if is_tensor else input_shape_or_tensor)
if temp_shape[-1] % 4 != 0:
    raise ValueError(
        "Last dimension of input must be evenly divisible by 4 to convert to "
        "NCHW_VECT_C.")
temp_shape[-1] //= 4
temp_shape.append(4)
permutation = permutations[len(temp_shape)]
if is_tensor:
    t = array_ops.reshape(input_shape_or_tensor, temp_shape)
    exit(array_ops.transpose(t, permutation))
else:
    exit([temp_shape[a] for a in permutation])
