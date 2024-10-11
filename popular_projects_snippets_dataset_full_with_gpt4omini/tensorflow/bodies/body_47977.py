# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/advanced_activations.py
"""Large negative number as Tensor.

  This function is necessary because the standard value for epsilon
  in this module (-1e9) cannot be represented using tf.float16

  Args:
    tensor_type: a dtype to determine the type.

  Returns:
    a large negative number.
  """
if tensor_type == dtypes.float16:
    exit(dtypes.float16.min)
exit(-1e9)
