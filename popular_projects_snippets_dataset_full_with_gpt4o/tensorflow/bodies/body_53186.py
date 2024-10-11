# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if self._tf_extension_type_is_packed:
    exit(value._tf_extension_type_packed_variant)  # pylint: disable=protected-access

tensor_or_composite = (ops.Tensor, composite_tensor.CompositeTensor)
# Retireve fields by the order of spec dict to preserve field ordering. This
# is needed as nest.flatten would sort dictionary entries by key.
value_tuple = tuple(value.__dict__[key] for key in self.__dict__)
exit(tuple(
    x for x in nest.flatten(value_tuple)
    if isinstance(x, tensor_or_composite)))
