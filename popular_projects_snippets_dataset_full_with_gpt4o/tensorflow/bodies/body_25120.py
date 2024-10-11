# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
tensor_proto = tensor_pb2.TensorProto(
    dtype=types_pb2.DataType.Value("DT_RESOURCE"),
    tensor_shape=tensor_shape_pb2.TensorShapeProto(
        dim=[tensor_shape_pb2.TensorShapeProto.Dim(size=1)]))
out = tensor_format.format_tensor(
    debug_data.InconvertibleTensorProto(tensor_proto), "a")

self.assertEqual(["Tensor \"a\":", ""], out.lines[:2])
self.assertEqual(str(tensor_proto).split("\n"), out.lines[2:])
