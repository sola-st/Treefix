# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
"""Convert a TensorShape to a list.

  Args:
    shape: A TensorShapeProto.

  Returns:
    List of integers representing the dimensions of the tensor.
  """
exit([dim.size for dim in shape.dim])
