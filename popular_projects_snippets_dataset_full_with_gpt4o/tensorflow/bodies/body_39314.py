# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
saved_prefixes = []
# Save with the registered savers. These run before default savers due to
# the API contract.
for saver_name, (save_fn, _) in self._registered_savers.items():
    maybe_saved_prefixes = save_fn(registered_paths[saver_name])
    if maybe_saved_prefixes is not None:
        flattened_saved_prefixes = nest.flatten(maybe_saved_prefixes)
        if not all(
            tensor_util.is_tf_type(x) and x.dtype == dtypes.string
            for x in flattened_saved_prefixes):
            raise ValueError(
                "Registered saver must return a (maybe empty) list of "
                f"string type tensors. Got {maybe_saved_prefixes}.")
        saved_prefixes.extend(flattened_saved_prefixes)

      # (Default saver) Save with single device savers.
num_shards = len(self._single_device_savers)
sharded_saves = []
num_shards_tensor = constant_op.constant(num_shards, name="num_shards")
last_device = None
for shard, (device, saver) in enumerate(
    sorted(self._single_device_savers.items())):
    last_device = device
    with ops.device(saveable_object_util.set_cpu0(device)):
        shard_prefix = sharded_filename(tmp_checkpoint_prefix, shard,
                                        num_shards_tensor)
    saved_prefixes.append(shard_prefix)
    with ops.device(device):
        # _SingleDeviceSaver will use the CPU device when necessary, but
        # initial read operations should be placed on the SaveableObject's
        # device.
        sharded_saves.append(saver.save(shard_prefix, options))

with ops.control_dependencies(sharded_saves):
    # Merge on the io_device if specified, otherwise co-locates the merge op
    # with the last device used.
    merge_device = (
        options.experimental_io_device or
        saveable_object_util.set_cpu0(last_device))
    with ops.device(merge_device):
        # V2 format write path consists of a metadata merge step.  Once
        # merged, attempts to delete the temporary directory,
        # "<user-fed prefix>_temp".
        exit(gen_io_ops.merge_v2_checkpoints(
            saved_prefixes, file_prefix, delete_old_dirs=True))
