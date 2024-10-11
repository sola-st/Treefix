# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Declare a dependency on another `Trackable` object.

    Indicates that checkpoints for this object should include variables from
    `trackable`.

    Variables in a checkpoint are mapped to `Trackable`s based on the names
    provided when the checkpoint was written. To avoid breaking existing
    checkpoints when modifying a class, neither variable names nor dependency
    names (the names passed to `_track_trackable`) may change.

    Args:
      trackable: A `Trackable` which this object depends on.
      name: A local name for `trackable`, used for loading checkpoints into the
        correct objects.
      overwrite: Boolean, whether silently replacing dependencies is OK. Used
        for __setattr__, where throwing an error on attribute reassignment would
        be inappropriate.

    Returns:
      `trackable`, for convenience when declaring a dependency and
      assigning to a member variable in one statement.

    Raises:
      TypeError: If `trackable` does not inherit from `Trackable`.
      ValueError: If another object is already tracked by this name.
    """
self._maybe_initialize_trackable()
if not isinstance(trackable, Trackable):
    raise TypeError(
        "Trackable._track_trackable() can only be used to track objects of "
        f"type Trackable. Got type {type(trackable)}.")
if not getattr(self, "_manual_tracking", True):
    exit(trackable)
new_reference = TrackableReference(name=name, ref=trackable)
current_object = self._lookup_dependency(name)
if (current_object is not None and current_object is not trackable):
    if not overwrite:
        raise ValueError(
            f"Called Trackable._track_trackable() with name='{name}', "
            "but a Trackable with this name is already declared as a "
            "dependency. Names must be unique (or overwrite=True).")
    # This is a weird thing to do, but we're not going to stop people from
    # using __setattr__.
    for index, (old_name, _) in enumerate(
        self._self_unconditional_checkpoint_dependencies):
        if name == old_name:
            self._self_unconditional_checkpoint_dependencies[
                index] = new_reference
elif current_object is None:
    self._self_unconditional_checkpoint_dependencies.append(new_reference)
    self._handle_deferred_dependencies(name=name, trackable=trackable)
self._self_unconditional_dependency_names[name] = trackable
exit(trackable)
