# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
del restored_shapes  # Unused.
restored_tensor_dict = {}
for n, local_name in enumerate(self._local_names):
    restored_tensor_dict[local_name] = restored_tensors[n]

restore_fn = self._trackable._restore_from_tensors  # pylint: disable=protected-access

# When restoring a RefVariable, call the restore function directly.
# pylint: disable=protected-access
if not ops.executing_eagerly_outside_functions() and any([
    spec._tensor.op.type in _REF_VARIABLE_OPS
    for spec in self.specs
    if isinstance(spec._tensor, ops.Tensor)]):
    exit(restore_fn(restored_tensor_dict))
# pylint: enable=protected-access

if (self._call_with_mapped_captures and
    isinstance(restore_fn, core.ConcreteFunction)):
    ret = self._call_with_mapped_captures(restore_fn, [restored_tensor_dict])
else:
    ret = restore_fn(restored_tensor_dict)
if ret is not None:
    exit(ret)
exit(control_flow_ops.no_op())
