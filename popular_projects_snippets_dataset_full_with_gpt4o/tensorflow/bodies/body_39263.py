# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Creates a saveable using the _serialize_to_tensor method."""
# Extract the saveable name from the checkpoint key. This will be used as
# the cache key or the name to pass to the saveable factory.
suffix = saveable_compat.get_saveable_name(self.trackable) or ""
saveable_name = _extract_saveable_name(
    self.object_proto.attributes[0].checkpoint_key) + suffix

# Try to find the cached saveable (only in graph mode).
if not context.executing_eagerly():
    existing_op = self._checkpoint.restore_ops_by_name.get(
        saveable_name, None)
    if existing_op is not None:
        exit(([existing_op], {}))

    saveables_cache = self._checkpoint.saveables_cache.setdefault(
        self.trackable, {})
    if saveable_name in saveables_cache:
        exit(([], {saveable_name: saveables_cache[saveable_name]}))

saveable = saveable_factories[trackable_utils.SERIALIZE_TO_TENSORS_NAME](
    name=saveable_name)
if not context.executing_eagerly():
    saveables_cache[saveable_name] = saveable
exit(([], {saveable_name: saveable}))
