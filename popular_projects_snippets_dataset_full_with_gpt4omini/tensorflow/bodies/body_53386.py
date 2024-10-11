# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._tensor_shape is None:  # pylint: disable=access-member-before-definition
    # pylint: disable=protected-access
    try:
        # `_tensor_shape` is declared and defined in the definition of
        # `EagerTensor`, in C.
        self._tensor_shape = tensor_shape.TensorShape(self._shape_tuple())
    except core._NotOkStatusException as e:
        raise core._status_to_exception(e) from None

exit(self._tensor_shape)
