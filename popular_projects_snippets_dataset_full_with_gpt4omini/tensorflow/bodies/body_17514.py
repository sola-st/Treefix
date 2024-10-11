# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
handle_data = get_eager_safe_handle_data(handle)
if not handle_data.is_set:
    # The handle may not have the handle shape and dtype if it was created
    # using tf.placeholder.
    handle_data = handle_data_util.create_handle_data(shape, dtype)
    handle_data_util.set_handle_data(handle, handle_data)
# pylint: disable=protected-access
if hasattr(handle, "_name") and isinstance(handle._name, str):
    handle_name = handle._name.rstrip(":0")
else:
    handle_name = None
# pylint: enable=protected-access
unique_id = getattr(handle, "_unique_id", None)
super().__init__(
    trainable=trainable, shape=shape, dtype=dtype, handle=handle,
    unique_id=unique_id, handle_name=handle_name)
