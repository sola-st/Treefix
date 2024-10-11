# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Runs restore ops for `trackable`'s attributes."""
# When graph building, we don't add any restore ops to the graph until
# run_restore_ops/initialize_or_restore on the status object for name-based
# checkpoints.
assert context.executing_eagerly()
for saveable in self.globally_named_object_attributes(trackable):
    restored_tensors = []
    tensor_missing = False
    for spec in saveable.specs:
        if spec.name in self.dtype_map:
            with ops.device("cpu:0"):
                restored, = io_ops.restore_v2(
                    prefix=self.save_path,
                    tensor_names=[spec.name],
                    shape_and_slices=[""],
                    dtypes=[self.dtype_map[spec.name]],
                    name="%s_checkpoint_read" % (spec.name,))
            restored_tensors.append(array_ops.identity(restored))
        else:
            tensor_missing = True

    if tensor_missing:
        # Record that this variable didn't match so assertions will fail.
        self.unused_attributes.setdefault(trackable, []).append(saveable.name)
    else:
        # Ignores values missing from the checkpoint, as with object-based
        # restore. Status assertions can be used to check exact matches,
        # although it's unlikely to ever happen for name-based checkpoints.
        saveable.restore(
            restored_tensors=restored_tensors, restored_shapes=None)
