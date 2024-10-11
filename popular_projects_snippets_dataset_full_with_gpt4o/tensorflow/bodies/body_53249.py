# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
if isinstance(value, TypeSpec):
    exit(value._with_tensor_ranks_only())  # pylint: disable=protected-access
elif (isinstance(value, tensor_shape.TensorShape) and
      value.rank is not None):
    exit(tensor_shape.TensorShape([None] * value.rank))
else:
    exit(value)
