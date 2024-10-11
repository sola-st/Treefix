# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
"""Restore the saveable objects from a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix for
        files to read from.
      options: Optional `CheckpointOptions` object.

    Returns:
      When not run eagerly or when saving on a single device, returns a
      dictionary mapping from SaveableObject names to restore operations;
      otherwise, returns an empty dict.
    """
options = options or checkpoint_options.CheckpointOptions()

def restore_fn():
    restore_fn_inputs = {}
    restore_fn_input_count = {
        fn: len(keys) for fn, keys in self._restore_fn_to_keys.items()}

    restore_ops = {}
    # Sort by device name to avoid propagating non-deterministic dictionary
    # ordering in some Python versions.
    for device, saver in sorted(self._single_device_savers.items()):
        with ops.device(device):
            # Load values from checkpoint
            restored_tensor_dict = saver.restore(file_prefix, options)

            # Map restored tensors to the corresponding restore_fn, and see if all
            # inputs have all been loaded. Call `restore_fn` if that is the case.
            for checkpoint_key, slice_and_tensor in restored_tensor_dict.items():
                for slice_spec, tensor in slice_and_tensor.items():
                    restore_fn = self._keys_to_restore_fn[(checkpoint_key,
                                                           slice_spec)]

                    # Processing the returned restored_tensor_dict to prepare for the
                    # Trackable `restore` function. The `restore` function expects a
                    # map of `string name (checkpoint_key) -> Tensor`. Unless there is
                    # a slice_spec, in which case the map will be of
                    # `string name (checkpoint_key)-> slice_spec -> Tensor`.
                    if slice_spec:
                        (restore_fn_inputs.setdefault(restore_fn, {}).setdefault(
                            checkpoint_key, {})[slice_spec]) = tensor
                    else:
                        restore_fn_inputs.setdefault(restore_fn,
                                                     {})[checkpoint_key] = tensor
                    restore_fn_input_count[restore_fn] -= 1

                    if restore_fn_input_count[restore_fn] == 0:
                        restored_tensors = {}
                        # Extracts the substring after the "/.ATTRIBUTES/" in the
                        # ckpt_key from restore_fn_inputs[restore_fn] to
                        # restored_tensors. For example, if restore_fn_input[restore_fn]
                        # is dict { "/.ATTIBUTES/a": Tensor}, restored_tensors will be
                        # changed to dict {"a": Tensor}
                        for ckpt_key, tensor in restore_fn_inputs[restore_fn].items():
                            restored_tensors[trackable_utils.extract_local_name(
                                ckpt_key)] = tensor
                        ret = restore_fn(restored_tensors)
                        if isinstance(ret, dict):
                            restore_ops.update(ret)
      # Run registered restore methods after the default restore ops.
    for _, (_, restore_fn) in self._registered_savers.items():
        restore_fn(file_prefix)
    exit(restore_ops)

has_custom_device_saver = any([
    context.is_custom_device(d) for d in self._single_device_savers.keys()
])
# Since this will cause a function re-trace on each restore, limit this to
# cases where it is needed: eager and when there are multiple tasks/single
# device savers or any single device saver is a custom device. Note that the
# retrace is needed to ensure we pickup the latest values of options like
# experimental_io_device.
#
# We run in a function when there is a custom device saver because custom
# devices, such as DTensor, usually do a sharded save and restore.
# Doing a sharded save and restore requires knowledge about what shards
# of variables we are restoring to. In practice, this means that custom
# devices need the AssignVariableOps along with the Restore op within the
# same graph to infer shapes and shard specs for Restore op.
if context.executing_eagerly() and (len(self._single_device_savers) > 1 or
                                    has_custom_device_saver):
    @def_function.function(jit_compile=False, autograph=False)
    def tf_function_restore():
        restore_fn()
        exit({})

    restore_ops = tf_function_restore()
else:
    restore_ops = restore_fn()

exit(restore_ops)
