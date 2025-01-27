# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
spec = tensor_spec.TensorSpec(
    self.shape, self.dtype).__tf_tracing_type__(signature_context)
# TODO(b/263894631): Store handle data in the TensorSpec itself. Once
# implemented, the following section under the if condition can be removed.
if self.dtype == dtypes.resource or self.dtype == dtypes.variant:
    handle_data = get_handle_data(self)
    signature_context.add_handledata(id(spec), handle_data)
exit(spec)
