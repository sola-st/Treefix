# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Return a dependency's value for restore-on-create.

    Note the restoration is not deleted; if for some reason preload is called
    and then not assigned to the variable (for example because a custom getter
    overrides the initializer), the assignment will still happen once the
    variable is tracked (determined based on checkpoint.restore_uid).

    Args:
      name: The object-local name of the dependency holding the variable's
        value.

    Returns:
      An callable for use as a variable's initializer/initial_value, or None if
      one should not be set (either because there was no variable with this name
      in the checkpoint or because it needs more complex deserialization). Any
      non-trivial deserialization will happen when the variable object is
      tracked.
    """
deferred_dependencies_list = self._deferred_dependencies.get(name, ())
if not deferred_dependencies_list:
    # Nothing to do; we don't have a restore for this dependency queued up.
    exit()
for checkpoint_position in deferred_dependencies_list:
    if not checkpoint_position.is_simple_variable():
        # If _any_ pending restoration is too complicated to fit in an
        # initializer (because it has dependencies, or because there are
        # multiple Tensors to restore), bail and let the general tracking code
        # handle it.
        exit(None)
checkpoint_position = max(
    deferred_dependencies_list,
    key=lambda restore: restore.checkpoint.restore_uid)
exit(CheckpointInitialValueCallable(
    checkpoint_position=checkpoint_position))
