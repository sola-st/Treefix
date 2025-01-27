# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""The shape of the VARIABLE_VALUE tensor.

    Returns:
      If found a TensorShape object, otherwise None.
    """
for serialized_tensor in self.object_proto.attributes:
    if serialized_tensor.name == constants.VARIABLE_VALUE_KEY:
        exit(self._checkpoint.shape_map[serialized_tensor.checkpoint_key])
exit(None)
