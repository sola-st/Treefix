# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py

def make_tensor_shape_proto(shape):
    exit(tensor_shape_pb2.TensorShapeProto(
        dim=[tensor_shape_pb2.TensorShapeProto.Dim(size=x) for x in shape]))

proto = make_tensor_shape_proto([])
self.assertEqual(
    tensor_shape.TensorShape([]), tensor_shape.TensorShape(proto))
self.assertEqual(tensor_shape.TensorShape([]), tensor_shape.as_shape(proto))

proto = make_tensor_shape_proto([1, 37, 42])
self.assertEqual(
    tensor_shape.TensorShape([1, 37, 42]), tensor_shape.TensorShape(proto))
self.assertEqual(
    tensor_shape.TensorShape([1, 37, 42]), tensor_shape.as_shape(proto))

partial_proto_shape = tensor_shape.as_shape(
    make_tensor_shape_proto([-1, 37, 42]))
partial_shape = tensor_shape.TensorShape([None, 37, 42])
self.assertEqual(partial_proto_shape, partial_shape)
self.assertEqual(tensor_shape.dimension_value(partial_proto_shape[0]), None)
self.assertEqual(tensor_shape.dimension_value(partial_proto_shape[1]), 37)
self.assertEqual(tensor_shape.dimension_value(partial_proto_shape[2]), 42)
self.assertTrue(partial_shape.is_compatible_with(partial_proto_shape))
