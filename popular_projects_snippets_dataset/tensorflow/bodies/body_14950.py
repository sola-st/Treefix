# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Constructs a graph mode TensorArray.

    Args:
      dtype: (required) data type of the TensorArray.
      size: (optional) int32 scalar `Tensor`: the size of the TensorArray.
        Required if flow is not provided.
      dynamic_size: (optional) Python bool: If true, writes to the TensorArray
        can grow the TensorArray past its initial size.  Default: False.
      clear_after_read: (optional) unused. Not supported in TensorLists.
      tensor_array_name: (optional) unused.
      handle: (optional) Must always be None.
      flow: (optional) A variant `Tensor` scalar for a TensorList.
      infer_shape: (optional, default: True) If True, shape inference is
        enabled.  In this case, all elements must have the same shape.
      element_shape: (optional, default: None) A `TensorShape` object specifying
        the shape constraints of each of the elements of the TensorArray. Need
        not be fully defined.
      colocate_with_first_write_call: (optional). unused.
      name: (optional) A name for the operation.

    Raises:
      ValueError: if both handle and tensor_array_name are provided.
      TypeError: if handle is provided but is not a Tensor.
    """
assert handle is None
del handle
del clear_after_read
del tensor_array_name
del colocate_with_first_write_call

self._dynamic_size = dynamic_size
self._size = size

if (flow is not None and
    (not isinstance(flow, ops.Tensor) or flow.dtype != dtypes.variant)):
    raise TypeError(
        f"Expected `flow` to be a variant tensor, but received `{flow.dtype}` "
        f"instead.")
if flow is None and size is None:
    raise ValueError("Argument `size` must be provided if argument `flow` "
                     "is not provided.")
if flow is not None and size is not None:
    raise ValueError("Cannot provide both `flow` and `size` arguments "
                     "at the same time.")
if flow is not None and element_shape is not None:
    raise ValueError(
        "Cannot provide both `flow` and `element_shape` arguments"
        "at the same time.")

self._dtype = dtypes.as_dtype(dtype).base_dtype

# Record the current static shape for the array elements. The element
# shape is defined either by `element_shape` or the shape of the tensor
# of the first write. If `infer_shape` is true, all writes checks for
# shape equality.
self._element_shape = [tensor_shape.as_shape(element_shape)]
self._infer_shape = infer_shape
with ops.name_scope(name, "TensorArrayV2", [size, flow]) as scope:
    if flow is None:
        self._flow = list_ops.tensor_list_reserve(
            element_shape=element_shape,
            num_elements=size,
            element_dtype=dtype,
            name=scope)
    else:
        self._flow = flow

    # For backwards compatibility.
self._colocate_with_first_write_call = None
self._colocate_with = None
