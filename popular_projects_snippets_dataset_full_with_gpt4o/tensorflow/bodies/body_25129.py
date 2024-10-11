# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
tensor_proto = tensor_pb2.TensorProto(
    dtype=types_pb2.DataType.Value("DT_FLOAT"),
    tensor_shape=tensor_shape_pb2.TensorShapeProto(
        dim=[tensor_shape_pb2.TensorShapeProto.Dim(size=1)]))
out = tensor_format.format_tensor(
    debug_data.InconvertibleTensorProto(tensor_proto, False), "a")

self.assertEqual(["Tensor \"a\":", "", "Uninitialized tensor:"],
                 out.lines[:3])

with self.assertRaisesRegex(
    AttributeError, "tensor_metadata is not available in annotations"):
    tensor_format.locate_tensor_element(out, [0])
