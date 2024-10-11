# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Create value `Tensor`s for this object's attributes.

    Does not require that the Python object has been created. Used for
    restore-on-create when executing eagerly.

    Args:
      shape_and_slices: A dict mapping from object attribute names to a shape
        and slice string that will be passed to a RestoreV2 op. If the dict is
        None or if an object attribute is not in the dict, the full tensor will
        be restored.

    Returns:
      A dictionary mapping from object attribute names to `Tensor`s.
    """
value_tensors = {}
for serialized_tensor in self.object_proto.attributes:
    checkpoint_key = serialized_tensor.checkpoint_key
    dtype = self._checkpoint.dtype_map[checkpoint_key]
    base_type = dtype.base_dtype
    io_device = self._checkpoint.options.experimental_io_device or "cpu:0"
    with ops.init_scope():
        with ops.device(io_device):
            # Run the restore itself on the io_device(CPU or specified).
            if (shape_and_slices is not None and
                serialized_tensor.name in shape_and_slices):
                shape_and_slice = shape_and_slices[serialized_tensor.name]
            else:
                shape_and_slice = ""
            value, = io_ops.restore_v2(
                prefix=self._checkpoint.save_path_tensor,
                tensor_names=[checkpoint_key],
                shape_and_slices=[shape_and_slice],
                dtypes=[base_type],
                name="%s_checkpoint_read" % (serialized_tensor.name,))
        # Copy the value to the current device if necessary.
        value_tensors[serialized_tensor.name] = array_ops.identity(value)
exit(value_tensors)
