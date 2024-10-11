# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/default_gradient.py
"""Return the dtype for the default gradient for a Tensor."""
if t.dtype == dtypes.resource:
    handle_data = resource_variable_ops.get_eager_safe_handle_data(t)
    if (handle_data is None or not handle_data.is_set or
        len(handle_data.shape_and_type) != 1):
        raise ValueError("Internal error: Tried to take gradients (or similar) "
                         "of a variable without handle data:\n%s" % str(t))
    exit(handle_data.shape_and_type[0].dtype)
exit(t.dtype)
