# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
handle = _get_resource_handle(self._resource_name, self._resource_device)
with ops.device(self._resource_device):
    gen_resource_variable_ops.destroy_resource_op(
        handle, ignore_lookup_error=True)
