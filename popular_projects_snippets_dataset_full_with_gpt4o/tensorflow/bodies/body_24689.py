# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Load a tensor from an Event proto.

  Args:
    event: The Event proto, assumed to hold a tensor value in its
        summary.value[0] field.

  Returns:
    The tensor value loaded from the event file, as a `numpy.ndarray`, if
    representation of the tensor value by a `numpy.ndarray` is possible.
    For uninitialized Tensors, returns `None`. For Tensors of data types that
    cannot be represented as `numpy.ndarray` (e.g., `tf.resource`), return
    the `TensorProto` protobuf object without converting it to a
    `numpy.ndarray`.
  """

tensor_proto = event.summary.value[0].tensor
shape = tensor_util.TensorShapeProtoToList(tensor_proto.tensor_shape)
num_elements = 1
for shape_dim in shape:
    num_elements *= shape_dim

if tensor_proto.tensor_content or tensor_proto.string_val or not num_elements:
    # Initialized tensor or empty tensor.
    if tensor_proto.dtype == types_pb2.DT_RESOURCE:
        tensor_value = InconvertibleTensorProto(tensor_proto)
    else:
        try:
            tensor_value = tensor_util.MakeNdarray(tensor_proto)
        except KeyError:
            tensor_value = InconvertibleTensorProto(tensor_proto)
else:
    # Uninitialized tensor or tensor of unconvertible data type.
    tensor_value = InconvertibleTensorProto(tensor_proto, False)

exit(tensor_value)
