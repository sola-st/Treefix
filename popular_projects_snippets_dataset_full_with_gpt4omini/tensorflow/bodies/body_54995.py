# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/common_shapes_test.py
unknown = tensor_shape.unknown_shape()
shape_0 = tensor_shape.TensorShape([])
shape_1 = tensor_shape.TensorShape([1])
# pylint: disable=invalid-name
shape_U = tensor_shape.TensorShape([None])
shape_1xU = tensor_shape.TensorShape([1, None])
shape_Ux1 = tensor_shape.TensorShape([None, 1])
shape_4xU = tensor_shape.TensorShape([4, None])
shape_Ux4 = tensor_shape.TensorShape([None, 4])
# pylint: enable=invalid-name

# Tensors with same shape should have the same broadcast result.
for shape in (shape_U, shape_1xU, shape_Ux1, shape_4xU, shape_Ux4):
    self._assert_broadcast_with_unknown_dims(
        expected=shape, shape1=shape, shape2=shape)

# [] and [1] act like identity.
for identity in (shape_0, shape_1):
    for shape in (shape_U, shape_1xU, shape_Ux1, shape_4xU, shape_Ux4):
        self._assert_broadcast_with_unknown_dims(
            expected=shape, shape1=identity, shape2=shape)

    # Unknown in, unknown out.
for shape in (shape_U, shape_1xU, shape_Ux1, shape_4xU, shape_Ux4):
    self._assert_broadcast_with_unknown_dims(
        expected=unknown, shape1=shape, shape2=unknown)

self._assert_broadcast_with_unknown_dims(
    expected=shape_1xU, shape1=shape_U, shape2=shape_1xU)
shape_UxU = tensor_shape.TensorShape([None, None])  # pylint: disable=invalid-name
self._assert_broadcast_with_unknown_dims(
    expected=shape_UxU, shape1=shape_U, shape2=shape_Ux1)
self._assert_broadcast_with_unknown_dims(
    expected=shape_4xU, shape1=shape_U, shape2=shape_4xU)
self._assert_broadcast_with_unknown_dims(
    expected=shape_Ux4, shape1=shape_U, shape2=shape_Ux4)
self._assert_broadcast_with_unknown_dims(
    expected=shape_UxU, shape1=shape_1xU, shape2=shape_Ux1)
self._assert_broadcast_with_unknown_dims(
    expected=shape_4xU, shape1=shape_1xU, shape2=shape_4xU)
self._assert_broadcast_with_unknown_dims(
    expected=shape_Ux4, shape1=shape_1xU, shape2=shape_Ux4)
self._assert_broadcast_with_unknown_dims(
    expected=shape_4xU, shape1=shape_Ux1, shape2=shape_4xU)
self._assert_broadcast_with_unknown_dims(
    expected=shape_Ux4, shape1=shape_Ux1, shape2=shape_Ux4)
shape_4x4 = tensor_shape.TensorShape([4, 4])
self._assert_broadcast_with_unknown_dims(
    expected=shape_4x4, shape1=shape_4xU, shape2=shape_Ux4)
