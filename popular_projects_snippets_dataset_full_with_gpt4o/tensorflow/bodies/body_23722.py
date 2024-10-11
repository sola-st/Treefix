# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Pop and load any deferred checkpoint restores into `trackable`.

    This method does not add a new dependency on `trackable`, but it does
    check if any outstanding/deferred dependencies have been queued waiting for
    this dependency to be added (matched based on `name`). If so,
    `trackable` and its dependencies are restored. The restorations are
    considered fulfilled and so are deleted.

    `_track_trackable` is more appropriate for adding a
    normal/unconditional dependency, and includes handling for deferred
    restorations. This method allows objects such as `Optimizer` to use the same
    restoration logic while managing conditional dependencies themselves, by
    overriding `_checkpoint_dependencies` and `_lookup_dependency` to change the
    object's dependencies based on the context it is saved/restored in (a single
    optimizer instance can have state associated with multiple graphs).

    Args:
      name: The name of the dependency within this object (`self`), used to
        match `trackable` with values saved in a checkpoint.
      trackable: The Trackable object to restore (inheriting from `Trackable`).
    """
self._maybe_initialize_trackable()
trackable._maybe_initialize_trackable()  # pylint: disable=protected-access
deferred_dependencies_list = self._deferred_dependencies.pop(name, ())
for checkpoint_position in sorted(
    deferred_dependencies_list,
    key=lambda restore: restore.checkpoint.restore_uid,
    reverse=True):
    checkpoint_position.restore(trackable)

# Pass on any name-based restores queued in this object.
for name_based_restore in sorted(
    self._self_name_based_restores,
    key=lambda checkpoint: checkpoint.restore_uid,
    reverse=True):
    trackable._name_based_attribute_restore(name_based_restore)  # pylint: disable=protected-access
