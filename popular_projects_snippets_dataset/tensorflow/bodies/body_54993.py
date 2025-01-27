# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/common_shapes_test.py
unknown = tensor_shape.unknown_shape()
shape_0 = tensor_shape.TensorShape([])
shape_1 = tensor_shape.TensorShape([1])
shape_4 = tensor_shape.TensorShape([4])
shape_1x4 = tensor_shape.TensorShape([1, 4])
shape_4x1 = tensor_shape.TensorShape([4, 1])
shape_3x4 = tensor_shape.TensorShape([3, 4])
shape_4x3 = tensor_shape.TensorShape([4, 3])

# Tensors with same shape should have the same broadcast result.
for shape in (
    shape_0, shape_1, shape_4, shape_1x4, shape_4x1, shape_3x4, shape_4x3):
    self._assert_broadcast(expected=shape, shape1=shape, shape2=shape)

# [] and [1] act like identity.
for identity in (shape_0, shape_1):
    for shape in (shape_4, shape_1x4, shape_4x1, shape_3x4, shape_4x3):
        self._assert_broadcast(expected=shape, shape1=identity, shape2=shape)

    # Unknown in, unknown out.
for shape in (shape_4, shape_1x4, shape_4x1, shape_3x4, shape_4x3):
    self._assert_broadcast(expected=unknown, shape1=shape, shape2=unknown)

self._assert_broadcast(expected=shape_1x4, shape1=shape_4, shape2=shape_1x4)
shape_4x4 = tensor_shape.TensorShape([4, 4])
self._assert_broadcast(expected=shape_4x4, shape1=shape_4, shape2=shape_4x1)
self._assert_broadcast(expected=shape_3x4, shape1=shape_4, shape2=shape_3x4)
self._assert_incompatible_broadcast(shape1=shape_4, shape2=shape_4x3)
self._assert_broadcast(
    expected=shape_4x4, shape1=shape_1x4, shape2=shape_4x1)
self._assert_broadcast(
    expected=shape_3x4, shape1=shape_1x4, shape2=shape_3x4)
self._assert_incompatible_broadcast(shape1=shape_1x4, shape2=shape_4x3)
self._assert_incompatible_broadcast(shape1=shape_4x1, shape2=shape_3x4)
self._assert_broadcast(
    expected=shape_4x3, shape1=shape_4x1, shape2=shape_4x3)
self._assert_incompatible_broadcast(shape1=shape_3x4, shape2=shape_4x3)
