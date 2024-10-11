# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Add ops to save the params per shard, for the V2 format.

    Note that the sharded save procedure for the V2 format is different from
    V1: there is a special "merge" step that merges the small metadata produced
    from each device.

    Args:
      checkpoint_prefix: scalar String Tensor.  Interpreted *NOT AS A FILENAME*,
        but as a prefix of a V2 checkpoint;
      per_device: A list of (device, BaseSaverBuilder.VarToSave) pairs, as
        returned by _GroupByDevices().

    Returns:
      An op to save the variables, which, when evaluated, returns the prefix
        "<user-fed prefix>" only and does not include the sharded spec suffix.
    """
# IMPLEMENTATION DETAILS: most clients should skip.
#
# Suffix for any well-formed "checkpoint_prefix", when sharded.
# Transformations:
# * Users pass in "save_path" in save() and restore().  Say "myckpt".
# * checkpoint_prefix gets fed <save_path><_SHARDED_SUFFIX>.
# * If checkpoint_prefix is a S3 bucket path ".part" is appended to it
# * Otherwise _temp/part is appended which is normalized relative to the OS
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
    _SHARDED_SUFFIX = array_ops.where(
        string_ops.regex_full_match(checkpoint_prefix, "^s3://.*"),
        constant_op.constant(".part"),
        constant_op.constant(os.path.normpath("_temp/part")))
    tmp_checkpoint_prefix = string_ops.string_join(
        [checkpoint_prefix, _SHARDED_SUFFIX])

num_shards = len(per_device)
sharded_saves = []
sharded_prefixes = []
num_shards_tensor = constant_op.constant(num_shards, name="num_shards")
last_device = None
for shard, (device, saveables) in enumerate(per_device):
    last_device = device
    with ops.device(saveable_object_util.set_cpu0(device)):
        sharded_filename = self.sharded_filename(tmp_checkpoint_prefix, shard,
                                                 num_shards_tensor)
        sharded_prefixes.append(sharded_filename)
        sharded_saves.append(self._AddSaveOps(sharded_filename, saveables))

with ops.control_dependencies([x.op for x in sharded_saves]):
    # Co-locates the merge step with the last device.
    with ops.device(saveable_object_util.set_cpu0(last_device)):
        # V2 format write path consists of a metadata merge step.  Once merged,
        # attempts to delete the temporary directory, "<user-fed prefix>_temp".
        merge_step = gen_io_ops.merge_v2_checkpoints(
            sharded_prefixes, checkpoint_prefix, delete_old_dirs=True)
        with ops.control_dependencies([merge_step]):
            # Returns the prefix "<user-fed prefix>" only.  DOES NOT include the
            # sharded spec suffix.
            exit(array_ops.identity(checkpoint_prefix))
