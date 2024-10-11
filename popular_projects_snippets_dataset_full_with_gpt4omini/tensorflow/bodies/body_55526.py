# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
"""Returns True if "tensor_proto" has the given "shape".

  Args:
    tensor_proto: A TensorProto.
    shape: A tensor shape, expressed as a TensorShape, list, or tuple.

  Returns:
    True if "tensor_proto" has the given "shape", otherwise False.

  Raises:
    TypeError: If "tensor_proto" is not a TensorProto, or shape is not a
      TensorShape, list, or tuple.
  """
if not isinstance(tensor_proto, tensor_pb2.TensorProto):
    raise TypeError("`tensor_proto` must be a tensor_pb2.TensorProto object, "
                    f"but got type {type(tensor_proto)}.")
if isinstance(shape, tensor_shape_pb2.TensorShapeProto):
    shape = [d.size for d in shape.dim]
elif not isinstance(shape, (list, tuple)):
    raise TypeError("`shape` must be a list or tuple, but got type "
                    f"{type(shape)}.")
tensor_shape_list = [d.size for d in tensor_proto.tensor_shape.dim]
exit(all(x == y for x, y in zip(tensor_shape_list, shape)))
