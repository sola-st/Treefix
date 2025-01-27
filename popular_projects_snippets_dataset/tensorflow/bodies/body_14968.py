# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Constructs a TensorArray compatible with eager execution.

    Args:
      dtype: (required) data type of the TensorArray.
      size: (optional) int32 scalar `Tensor`: the size of the TensorArray.
        Required if handle is not provided.
      dynamic_size: (optional) Python bool: If true, writes to the TensorArray
        can grow the TensorArray past its initial size.  Default: False.
      clear_after_read: Boolean (optional, default: True).  If True, clear
        TensorArray values after reading them.  This disables read-many
        semantics, but allows early release of memory.
      tensor_array_name: unused.
      handle: unsupported.
      flow: unsupported.
      infer_shape: used for error checking, same semantics as TensorArray.
      element_shape: used for error checking, same semantics as TensorArray.
      colocate_with_first_write_call: unsupported.
      name: unsupported.

    Raises:
      ValueError: handle or flow are supplied, or if size is not supplied.
    """

del (flow, tensor_array_name, name)  # Unused.

if handle is not None:
    raise ValueError("TensorArray handles are not supported when eager "
                     "execution is enabled.")
if size is None:
    raise ValueError("Size must be declared for TensorArrays when eager "
                     "execution is enabled.")

# These attributes are not meaningful when eager is enabled, but some
# library functions (e.g., those in control_flow_ops.py) access them to
# create new tensor arrays; as such, we define them for the sake of
# compatibility.
self._handle = None
# we assign a dummy value to _flow in case other code assumes it to be
# a Tensor
self._flow = constant_op.constant(0, dtype=dtypes.int32)
self._infer_shape = infer_shape
self._element_shape = tensor_shape.as_shape(element_shape)
self._colocate_with_first_write_call = colocate_with_first_write_call

self._dtype = dtypes.as_dtype(dtype).base_dtype
self._dynamic_size = dynamic_size or False
self._clear_after_read = (True
                          if clear_after_read is None else clear_after_read)
self._previously_read_indices = []

if isinstance(size, ops.EagerTensor):
    size = size.numpy()
self._tensor_array = [None for _ in range(size)]
