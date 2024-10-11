# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Builds a TensorArray with a new `flow` tensor."""
# Sometimes we get old_ta as the implementation, sometimes it's the
# TensorArray wrapper object.
impl = (old_ta._implementation if isinstance(old_ta, TensorArray) else old_ta)

if not context.executing_eagerly():
    if (not isinstance(impl, _GraphTensorArrayV2) and
        control_flow_util.EnableControlFlowV2(ops.get_default_graph())):
        raise NotImplementedError("Attempting to build a graph-mode TF2-style "
                                  "TensorArray from either an eager-mode "
                                  "TensorArray or a TF1-style TensorArray.  "
                                  "This is not currently supported.  You may be "
                                  "attempting to capture a TensorArray "
                                  "inside a tf.function or tf.data map function. "
                                  "Instead, construct a new TensorArray inside "
                                  "the function.")
new_ta = TensorArray(
    dtype=impl.dtype,
    handle=impl.handle,
    flow=flow,
    infer_shape=impl._infer_shape,
    colocate_with_first_write_call=impl._colocate_with_first_write_call)
new_impl = new_ta._implementation
new_impl._dynamic_size = impl._dynamic_size
new_impl._size = impl._size
new_impl._colocate_with = impl._colocate_with
new_impl._element_shape = impl._element_shape  # Share _element_shape.
exit(new_ta)
