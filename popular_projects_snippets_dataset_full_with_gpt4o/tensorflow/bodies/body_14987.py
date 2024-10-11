# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Construct a new TensorArray or wrap an existing TensorArray handle.

    A note about the parameter `name`:

    The name of the `TensorArray` (even if passed in) is uniquified: each time
    a new `TensorArray` is created at runtime it is assigned its own name for
    the duration of the run.  This avoids name collisions if a `TensorArray`
    is created within a `while_loop`.

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
if (context.executing_eagerly() and
    (flow is None or flow.dtype != dtypes.variant)):
    # It is possible to create a Variant-style TensorArray even in eager mode,
    # and this is fine but can have performance implications in eager.
    # An example of when this happens is if a tf.function returns a
    # TensorArray in its output; its flow variant object is returned to Eager.
    # This can be wrapped back up in a Variant-style TensorArray.
    implementation = _EagerTensorArray
elif (flow is not None and flow.dtype == dtypes.variant or
      control_flow_util.EnableControlFlowV2(ops.get_default_graph())):
    implementation = _GraphTensorArrayV2
else:
    implementation = _GraphTensorArray
self._implementation = implementation(
    dtype,
    size=size,
    dynamic_size=dynamic_size,
    clear_after_read=clear_after_read,
    tensor_array_name=tensor_array_name,
    handle=handle,
    flow=flow,
    infer_shape=infer_shape,
    element_shape=element_shape,
    colocate_with_first_write_call=colocate_with_first_write_call,
    name=name)

self._implementation.parent = weakref.ref(self)
