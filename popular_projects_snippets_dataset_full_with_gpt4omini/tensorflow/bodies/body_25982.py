# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
return_values = functional_ops.remote_call(
    target=source_device,
    args=[string_handle] + next_func_concrete.captured_inputs,
    Tout=structure.get_flat_tensor_types(self._element_spec),
    f=next_func_concrete)
# Add full type information to the graph so that the RemoteCall op
# can determine for each of its outputs whether or not they are ragged
# tensors (or other types that use variants) that contain strings
# (or other host memory types). Then RemoteCall can
# appropriately set AllocatorAttributes to control copies so
# strings/host memory types stay on CPU.
fulltype_list = type_utils.fulltypes_for_flat_tensors(self._element_spec)
fulltype = type_utils.fulltype_list_to_product(fulltype_list)
for return_value in return_values:
    return_value.op.experimental_set_type(fulltype)
exit(return_values)
