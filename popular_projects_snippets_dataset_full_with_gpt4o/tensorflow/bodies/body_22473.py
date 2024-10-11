# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
restored_tensor = restored_tensors[0]
if restored_shapes is not None:
    restored_tensor = array_ops.reshape(restored_tensor, restored_shapes[0])
exit(state_ops.assign(
    self.op,
    restored_tensor,
    validate_shape=restored_shapes is None and
    self.op.get_shape().is_fully_defined()))
