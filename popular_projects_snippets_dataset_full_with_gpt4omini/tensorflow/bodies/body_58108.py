# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Sets Tensor shape for each tensor if the shape is defined.

  Args:
    tensors: TensorFlow ops.Tensor.
    shapes: Dict of strings representing input tensor names to list of
      integers representing input shapes (e.g., {"foo": : [1, 16, 16, 3]}).

  Raises:
    ValueError:
      `shapes` contains an invalid tensor.
      `shapes` contains an invalid shape for a valid tensor.
  """
if shapes:
    tensor_names_to_tensor = {
        get_tensor_name(tensor): tensor for tensor in tensors
    }
    for name, shape in shapes.items():
        if name not in tensor_names_to_tensor:
            raise ValueError("Invalid tensor \'{}\' found in tensor shapes "
                             "map.".format(name))
        if shape is not None:
            tensor = tensor_names_to_tensor[name]
            try:
                tensor.set_shape(shape)
            except ValueError as error:
                message = ("The shape of tensor '{0}' cannot be changed from {1} to "
                           "{2}. {3}".format(name, tensor.shape, shape, str(error)))
                raise ValueError(message)
