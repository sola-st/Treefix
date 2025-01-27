# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Restore-on-create for a variable be saved with this `Trackable`.

    If the user has requested that this object or another `Trackable` which
    depends on this object be restored from a checkpoint (deferred loading
    before variable object creation), `initializer` may be ignored and the value
    from the checkpoint used instead.

    Args:
      name: A name for the variable. Must be unique within this object.
      shape: The shape of the variable.
      dtype: The data type of the variable.
      initializer: The initializer to use. Ignored if there is a deferred
        restoration stored in the Trackable.
      getter: The getter to wrap which actually fetches the variable.
      overwrite: If True, disables unique name and type checks.
      **kwargs_for_getter: Passed to the getter.

    Returns:
      The new variable object.

    Raises:
      ValueError: If the variable name is not unique.
    """
self._maybe_initialize_trackable()
with ops.init_scope():
    if context.executing_eagerly():
        # If this is a variable with a single Tensor stored in the checkpoint,
        # we can set that value as an initializer rather than initializing and
        # then assigning (when executing eagerly). This call returns None if
        # there is nothing to restore.
        checkpoint_initializer = self._preload_simple_restoration(name=name)
    else:
        checkpoint_initializer = None
    if (checkpoint_initializer is not None and
        not (isinstance(initializer, CheckpointInitialValueCallable) and
             (initializer.restore_uid > checkpoint_initializer.restore_uid))):
        # If multiple Trackable objects are "creating" the same variable
        # via the magic of custom getters, the one with the highest restore UID
        # (the one called last) has to make the final initializer. If another
        # custom getter interrupts this process by overwriting the initializer,
        # then we'll catch that when we call _track_trackable. So this is
        # "best effort" to set the initializer with the highest restore UID.
        initializer = checkpoint_initializer
new_variable = getter(
    name=name,
    shape=shape,
    dtype=dtype,
    initializer=initializer,
    **kwargs_for_getter)

# If we set an initializer and the variable processed it, tracking will not
# assign again. It will add this variable to our dependencies, and if there
# is a non-trivial restoration queued, it will handle that. This also
# handles slot variables.
if not overwrite or isinstance(new_variable, Trackable):
    exit(self._track_trackable(new_variable, name=name, overwrite=overwrite))
else:
    # TODO(allenl): Some variable types are not yet supported. Remove this
    # fallback once all get_variable() return types are Trackable.
    exit(new_variable)
