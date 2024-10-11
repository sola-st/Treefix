# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/common_shapes_test.py
s1 = tensor_shape.TensorShape([5])
s2 = tensor_shape.TensorShape([7])

unknown = tensor_shape.unknown_shape()
scalar = tensor_shape.TensorShape([])
expanded_scalar = tensor_shape.TensorShape([1])

# Tensors with same shape should have the same broadcast result.
for shape in (s1, s2, unknown, scalar, expanded_scalar):
    self._assert_broadcast(expected=shape, shape1=shape, shape2=shape)

# [] and [1] act like identity.
self._assert_broadcast(expected=s1, shape1=s1, shape2=scalar)
self._assert_broadcast(expected=s2, shape1=s2, shape2=scalar)
self._assert_broadcast(expected=s1, shape1=s1, shape2=expanded_scalar)
self._assert_broadcast(expected=s2, shape1=s2, shape2=expanded_scalar)

self._assert_broadcast(expected=unknown, shape1=s1, shape2=unknown)
self._assert_broadcast(expected=unknown, shape1=s2, shape2=unknown)

self._assert_broadcast(
    expected=expanded_scalar, shape1=scalar, shape2=expanded_scalar)

self._assert_incompatible_broadcast(shape1=s1, shape2=s2)
