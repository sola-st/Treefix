# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Constructs a graph mode TensorArray.

    Args:
      dtype: (required) data type of the TensorArray.
      size: (optional) int32 scalar `Tensor`: the size of the TensorArray.
        Required if handle is not provided.
      dynamic_size: (optional) Python bool: If true, writes to the TensorArray
        can grow the TensorArray past its initial size.  Default: False.
      clear_after_read: Boolean (optional, default: True).  If True, clear
        TensorArray values after reading them.  This disables read-many
        semantics, but allows early release of memory.
      tensor_array_name: (optional) Python string: the name of the TensorArray.
        This is used when creating the TensorArray handle.  If this value is
        set, handle should be None.
      handle: (optional) A `Tensor` handle to an existing TensorArray.  If this
        is set, tensor_array_name should be None. Only supported in graph mode.
      flow: (optional) A float `Tensor` scalar coming from an existing
        `TensorArray.flow`. Only supported in graph mode.
      infer_shape: (optional, default: True) If True, shape inference is
        enabled.  In this case, all elements must have the same shape.
      element_shape: (optional, default: None) A `TensorShape` object specifying
        the shape constraints of each of the elements of the TensorArray. Need
        not be fully defined.
      colocate_with_first_write_call: If `True`, the TensorArray will be
        colocated on the same device as the Tensor used on its first write
        (write operations include `write`, `unstack`, and `split`).  If `False`,
        the TensorArray will be placed on the device determined by the device
        context available during its initialization.
      name: A name for the operation (optional).

    Raises:
      ValueError: if both handle and tensor_array_name are provided.
      TypeError: if handle is provided but is not a Tensor.
    """
if handle is not None and tensor_array_name:
    raise ValueError(
        "Cannot provide both `handle` and `tensor_array_name` arguments at "
        "the same time.")
if handle is not None and not isinstance(handle, ops.Tensor):
    raise TypeError(
        f"Expected `handle` to be a Tensor, but got `{handle}` of type "
        f"`{type(handle)}` instead.")
if handle is None and size is None:
    raise ValueError(
        "Argument `size` must be provided if handle is not provided.")
if handle is not None and size is not None:
    raise ValueError("Cannot provide both a `handle` and `size` arguments "
                     "at the same time.")
if handle is not None and element_shape is not None:
    raise ValueError(
        "Cannot provide both `handle` and `element_shape` arguments "
        "at the same time.")
if handle is not None and dynamic_size is not None:
    raise ValueError(
        "Cannot provide both `handle` and `dynamic_size` arguments "
        "at the same time.")
if handle is not None and clear_after_read is not None:
    raise ValueError(
        "Cannot provide both `handle` and `clear_after_read` arguments "
        "at the same time.")

if clear_after_read is None:
    clear_after_read = True
self._dynamic_size = dynamic_size or False
self._dtype = dtypes.as_dtype(dtype).base_dtype

# Used to keep track of what tensors the TensorArray should be
# colocated with.  We choose to colocate the TensorArray with the
# first tensor written to it.
self._colocate_with_first_write_call = colocate_with_first_write_call
if colocate_with_first_write_call:
    self._colocate_with = []
else:
    self._colocate_with = None

# Record the current static shape for the array elements. The element
# shape is defined either by `element_shape` or the shape of the tensor
# of the first write. If `infer_shape` is true, all writes checks for
# shape equality.
self._element_shape = [tensor_shape.as_shape(element_shape)]
self._infer_shape = infer_shape
self._size = size
with ops.name_scope(name, "TensorArray", [handle, size, flow]) as scope:
    if handle is not None:
        self._handle = handle
        if flow is None:
            raise ValueError("flow must not be None if handle is not None.")
        self._flow = flow
    else:
        # Construct the TensorArray with an empty device.  The first
        # write into the TensorArray from a Tensor with a set device
        # will retroactively set the device value of this op.
        def create():
            """Create the TensorArray op."""
            exit(gen_data_flow_ops.tensor_array_v3(
                dtype=dtype,
                size=size,
                element_shape=element_shape,
                identical_element_shapes=infer_shape,
                dynamic_size=self._dynamic_size,
                clear_after_read=clear_after_read,
                tensor_array_name=tensor_array_name,
                name=scope))

        if colocate_with_first_write_call:
            with ops.device(None), ops.colocate_with(None, ignore_existing=True):
                self._handle, self._flow = create()
        else:
            self._handle, self._flow = create()
