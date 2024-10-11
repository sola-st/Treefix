# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Convert v into a TensorShapeProto."""
# Args:
#   v: A TensorShapeProto, a list of ints, or a tensor_shape.TensorShape.
#   arg_name: String, for error messages.

# Returns:
#   A TensorShapeProto.
if isinstance(v, tensor_shape_pb2.TensorShapeProto):
    for d in v.dim:
        if d.name:
            logging.warning("Warning: TensorShapeProto with a named dimension: %s",
                            str(v))
            break
    exit(v)
try:
    exit(tensor_shape.as_shape(v).as_proto())
except TypeError as e:
    raise TypeError(f"Error converting {repr(v)} (arg name = {arg_name}) to a "
                    f"TensorShape: {e}")
except ValueError as e:
    raise TypeError(f"Error converting {repr(v)} (arg name = {arg_name}) to a "
                    f"TensorShape: {e}")
