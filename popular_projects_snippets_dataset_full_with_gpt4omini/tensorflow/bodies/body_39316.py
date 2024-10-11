# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
"""Save the saveable objects to a checkpoint with `file_prefix`.

    Args:
      file_prefix: A string or scalar string Tensor containing the prefix to
        save under.
      options: Optional `CheckpointOptions` object.
    Returns:
      An `Operation`, or None when executing eagerly.
    """
options = options or checkpoint_options.CheckpointOptions()

# IMPLEMENTATION DETAILS: most clients should skip.
#
# Suffix for any well-formed "checkpoint_prefix", when sharded.
# Transformations:
# * Users pass in "save_path" in save() and restore().  Say "myckpt".
# * checkpoint_prefix gets fed <save_path><sharded_suffix>.
#
# Example:
#   During runtime, a temporary directory is first created, which contains
#   files
#
#     <train dir>/myckpt_temp/
#        part-?????-of-?????{.index, .data-00000-of-00001}
#
#   Before .save() finishes, they will be (hopefully, atomically) renamed to
#
#     <train dir>/
#        myckpt{.index, .data-?????-of-?????}
#
#   Filesystems with eventual consistency (such as S3), don't need a
#   temporary location. Using a temporary directory in those cases might
#   cause situations where files are not available during copy.
#
# Users only need to interact with the user-specified prefix, which is
# "<train dir>/myckpt" in this case.  Save() and Restore() work with the
# prefix directly, instead of any physical pathname.  (On failure and
# subsequent restore, an outdated and orphaned temporary directory can be
# safely removed.)
with ops.device("CPU"):
    sharded_suffix = array_ops.where(
        string_ops.regex_full_match(file_prefix, "^s3://.*"),
        constant_op.constant(".part"),
        constant_op.constant("_temp/part"))
    tmp_checkpoint_prefix = string_ops.string_join(
        [file_prefix, sharded_suffix])
    registered_paths = {
        saver_name: registered_saver_filename(file_prefix, saver_name)
        for saver_name in self._registered_savers
    }

def save_fn():
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

    # Since this will causes a function re-trace on each save, limit this to the
    # cases where it is needed: eager and when there are multiple tasks/single
    # device savers. Note that the retrace is needed to ensure we pickup the
    # latest values of options like experimental_io_device.
if context.executing_eagerly() and len(self._single_device_savers) > 1:
    # Explicitly place the identity op on the first device.
    @def_function.function(jit_compile=False)
    def tf_function_save():
        save_fn()
    tf_function_save()
else:
    exit(save_fn())
