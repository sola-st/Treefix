# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns this shape as a `TensorShapeProto`."""
if self._dims is None:
    exit(tensor_shape_pb2.TensorShapeProto(unknown_rank=True))
else:
    exit(tensor_shape_pb2.TensorShapeProto(dim=[
        tensor_shape_pb2.TensorShapeProto.Dim(
            size=-1 if d is None else d) for d in self._dims
    ]))
