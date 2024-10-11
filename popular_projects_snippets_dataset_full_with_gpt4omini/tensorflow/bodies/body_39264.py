# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Creates or caches SaveableObjects by matching the attribute names.

    The attribute name keys in the `saveable_factories` is used to find the
    corresponding attribute in the object proto. Attributes contain checkpoint
    keys which are passed to the factory function to generate the
    SaveableObject.

    Args:
      saveable_factories: a dict mapping attribute name to a callable factory
        function that produces a SaveableObject.

    Returns:
      A tuple of (
          existing_restore_ops: list,
          named_saveables: dict)
    """
# Name saveables based on the name this object had when it was checkpointed.
named_saveables = {}
existing_restore_ops = []

# Forward compatibility code: when loading a future checkpoint, there may
# be multiple SerializedTensors mapped to a single saveable.
created_compat_names = set()

for serialized_tensor in self.object_proto.attributes:
    if context.executing_eagerly():
        existing_op = None
    else:
        existing_op = self._checkpoint.restore_ops_by_name.get(
            serialized_tensor.checkpoint_key, None)
    if existing_op is not None:
        existing_restore_ops.append(existing_op)
        continue

    if any(serialized_tensor.name.startswith(name)
           for name in created_compat_names):
        continue  # Saveable has already been created for this tensor.

    # Only if we don't have cached ops for this SaveableObject, we'll see if
    # the SaveableObject itself has been cached. If not, we'll make it, and
    # either way we'll extract new ops from it (or if it has Python state to
    # restore, we'll run that).
    saveables_cache = self._checkpoint.saveables_cache
    if saveables_cache is None:
        # No SaveableObject caching when executing eagerly.
        saveable = None
    else:
        # If we've already created and cached a SaveableObject for this
        # attribute, we can re-use it to avoid re-creating some ops when graph
        # building.
        saveable_list = saveables_cache.get(self.trackable,
                                            {}).get(serialized_tensor.name,
                                                    (None,))
        if len(saveable_list) == 1:
            # Almost every attribute will have exactly one SaveableObject.
            saveable, = saveable_list
        else:
            # Don't use cached SaveableObjects for partitioned variables, which is
            # the only case where we'd have a list of SaveableObjects. Op caching
            # will catch them.
            saveable = None
    if saveable is not None:
        # The name of this attribute has changed, so we need to re-generate
        # the SaveableObject.
        if serialized_tensor.checkpoint_key not in saveable.name:
            saveable = None
            del saveables_cache[self.trackable]
    if saveable is None:
        # If there was no cached SaveableObject, create one.
        # Use the name to check if the Python object has the same attribute.
        saveable = _get_saveable_from_factory(saveable_factories,
                                              serialized_tensor,
                                              created_compat_names)
        if saveable is None:
            # Purposefully does not throw an exception if attributes have been
            # added or deleted. Stores unused attributes so an exception can be
            # raised if the user decides to check that everything in the
            # checkpoint was loaded.
            self._checkpoint.unused_attributes.setdefault(
                self._proto_id, []).append(serialized_tensor.name)
            continue
        if saveables_cache is not None:
            saveables_cache.setdefault(self.trackable,
                                       {})[serialized_tensor.name] = [saveable]
    named_saveables[serialized_tensor.checkpoint_key] = saveable

exit((existing_restore_ops, named_saveables))
