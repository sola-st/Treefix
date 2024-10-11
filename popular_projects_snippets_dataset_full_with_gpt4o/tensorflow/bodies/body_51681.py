# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Validates the `TensorInfo` proto.

    Checks if the `encoding` (`name` or `coo_sparse` or `type_spec`) and
    `dtype` fields exist and are non-empty.

    Args:
      tensor_info: `TensorInfo` protocol buffer to validate.

    Raises:
      AssertionError: If the `encoding` or `dtype` fields of the supplied
          `TensorInfo` proto are not populated.
    """
if tensor_info is None:
    raise AssertionError(
        "All TensorInfo protos used in the SignatureDefs must have the name "
        "and dtype fields set.")
if tensor_info.WhichOneof("encoding") is None:
    # TODO(soergel) validate each of the fields of coo_sparse
    raise AssertionError(
        f"Invalid `tensor_info`: {tensor_info}. All TensorInfo protos used "
        "in the SignatureDefs must have one of the 'encoding' fields (e.g., "
        "name or coo_sparse) set.")
if tensor_info.WhichOneof("encoding") == "composite_tensor":
    for component in tensor_info.composite_tensor.components:
        self._validate_tensor_info(component)
elif tensor_info.dtype == types_pb2.DT_INVALID:
    raise AssertionError(
        f"Invalid `tensor_info`: {tensor_info}. All TensorInfo protos used in"
        " the SignatureDefs must have the dtype field set.")
