# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Updates the shape of this KerasTensor. Mimics `tf.Tensor.set_shape()`."""
if not isinstance(shape, tensor_shape.TensorShape):
    shape = tensor_shape.TensorShape(shape)
if shape.dims is not None:
    dim_list = [dim.value for dim in shape.dims]
    for dim in range(len(dim_list)):
        if dim_list[dim] is None and self.shape.dims is not None:
            dim_list[dim] = self.shape.dims[dim]
    shape = tensor_shape.TensorShape(dim_list)
if not self.shape.is_compatible_with(shape):
    raise ValueError(
        "Keras symbolic input/output's shape %s is not"
        "compatible with supplied shape %s" %
        (self.shape, shape))
else:
    self._type_spec._shape = shape  # pylint: disable=protected-access
