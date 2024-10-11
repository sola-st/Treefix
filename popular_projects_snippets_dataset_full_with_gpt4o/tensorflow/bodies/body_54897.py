# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
exit(tensor_shape_pb2.TensorShapeProto(
    dim=[tensor_shape_pb2.TensorShapeProto.Dim(size=x) for x in shape]))
